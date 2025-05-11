# Python File Locker

Python File Locker is a secure command-line utility that allows users to lock (encrypt) and unlock files using password-based encryption. It offers a styled terminal interface using `rich`, and implements strong cryptographic standards via the `cryptography` library.

## Libraries Used

- `rich`: For interactive and styled command-line output
- `cryptography`: For password-based encryption and decryption

## Encryption Standard

- **Key Derivation**: PBKDF2-HMAC using SHA-256, with 100,000 iterations and a random salt
- **Encryption Scheme**: AES (via Fernet) for symmetric encryption with authentication

## Features

- Lock files with a password (adds `.locked` extension)
- Unlock encrypted files using the correct password
- Clone existing files
- Styled prompts, color-coded messages, and error handling
- Secure, hidden password input
- Path validation with smart suggestions

## Installation

Ensure you have Python 3.6 or newer installed.
Then, install the required packages:

```
pip install -r requirements.txt
```

### How to use

Simply run the file.

```
python project.py
```

### Testing

The project includes a test file named test_project.py, which contains tests for the project. These tests are designed using the `pytest` framework.

To run the tests, use the following command:
```
pytest test_project.py
```

Note: Even if you delete the test_file.txt it will be generated again automatically during testing.
