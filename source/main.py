import requests  # To make HTTP requests to the API
import hashlib   # To securely hash the password
import sys       # To access command-line arguments and exit the script

# Function to request data from the HaveIBeenPwned API using the first 5 characters of the hashed password
def req_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)  # Send GET request to the API
    if res.status_code != 200:
        # Raise error if the request failed
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again')
    return res

# Function to check if the remaining SHA1 hash tail exists in the response
def get_pwned_passwords_count(hashes, hash_to_check):
    # Parse each line of the response into hash suffix and count
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count  # Return the number of times the password was found
    return 0  # Return 0 if not found

# Function to check a given password against the HaveIBeenPwned database
def pwn_api_check(password):
    # Hash the password using SHA1 and convert it to uppercase hexadecimal
    sha1pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1pass[:5], sha1pass[5:]  # Split into first 5 characters and the rest
    response = req_api_data(first5_char)           # Send only the first 5 characters to the API
    return get_pwned_passwords_count(response, tail)  # Check if the remaining hash is in the result

# Main function to handle multiple passwords passed as command-line arguments
def main(args):
    for password in args:
        count = pwn_api_check(password)  # Check each password
        if count:
            print(f'{password} was found {count} times... you should probably change it! >:)')
        else:
            print(f'{password} was NOT found. Carry on! :)')
    return 'done!'

# Entry point of the script when run directly
if __name__ == '__main__':
    # Run main() with command-line arguments (excluding the script name itself)
    sys.exit(main(sys.argv[1:]))
