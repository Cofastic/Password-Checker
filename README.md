# 🔐 Pwned Password Checker (CLI Tool)

This is a simple Python command-line tool project to check if your passwords have been exposed in known data breaches using the [Have I Been Pwned](https://haveibeenpwned.com/) API. Your password is **never sent** directly to the API, only part of its SHA-1 hash is used, ensuring privacy.
---

## 📌 Features

- ✅ Checks if a password was leaked in a public breach
- 🔐 Uses the k-anonymity model for safe querying
- 📉 Reports how many times each password appeared in breaches
- 🧪 Lightweight, fast, and easy to run from terminal
- 📜 Clean, readable Python code

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Cofastic/Password-Checker.git
cd Password-Checker
```
Or download the <a href="https://github.com/Cofastic/Password-Checker/blob/main/source/passwordchecker.py"> ZIP </a> and extract it.

### 2. Install Python (if not already installed)
Check Python version:

```bash
python --version
```
If not installed, download it from: https://www.python.org/downloads/

Make sure to check "Add Python to PATH" during installation on Windows.

### 3. Install Required Package
Install the requests module (if you don't already have it):

```bash
pip install requests
```
## 🧑‍💻 Usage
Run the script followed by the passwords you want to check:

```bash
python passwordchecker.py password123 qwerty123 abc123
```
### 🔍 Example Output:
```bash
password123 was found 21765 times... you should probably change it! >:)
qwerty123 was found 98987 times... you should probably change it! >:)
abc123 was NOT found. Carry on! :)
done!
```

## ⚙️ How It Works
Password is hashed with SHA-1 using Python’s hashlib.

The first 5 characters of the hash are sent to the HaveIBeenPwned API.

The API returns all matching hash suffixes and breach counts.

The script checks if the full hash exists in the returned list.

✅ Your full password is never sent — only a hash prefix.

## 🛠 Advanced Usage
Check passwords from a text file (Unix-based):
```bash
for pw in $(cat passwords.txt); do python passwordchecker.py "$pw"; done
```

Check passwords from a text file (Windows CLI):
```bash
python passwordchecker.py passwords.txt
```
## ❓ Troubleshooting
ModuleNotFoundError: No module named 'requests'	-> Run pip install requests

'python' is not recognized ->	Use python3 instead, or check Python is in PATH

## 🔐 Security & Privacy
This script does not store any passwords or logs.
All queries use the k-anonymity protocol.
Meant for personal auditing or educational use only.
Do not use on someone else’s passwords without permission.

📄 License
MIT License. Free to use, modify, and share.

🙏 Credits
Troy Hunt for the Have I Been Pwned API.
