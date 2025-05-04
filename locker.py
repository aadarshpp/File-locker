import os
from cryptography.fernet import Fernet
from derive_key import get_derive_key

def encrypt_file(filepath: str, password: str):
    with open(filepath, 'rb') as f:
        data = f.read()

    salt = os.urandom(16)
    key = get_derive_key(password, salt)
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(filepath, 'wb') as f:
        f.write(salt + encrypted)

    os.rename(filepath, f"{filepath}.locked")
    print(f"Encrypted and locked {filepath}")

def decrypt_file(filepath: str, password: str) -> bool:

    with open(filepath, 'rb') as f:
        salt = f.read(16)
        encrypted_data = f.read()

    key = get_derive_key(password, salt)
    fernet = Fernet(key)
    try:
        decrypted = fernet.decrypt(encrypted_data)
    except Exception as e:
        print("Incorrect password or file is corrupted.")
        return False

    directory, filename = os.path.split(filepath)
    base_name, extension = os.path.splitext(filename)

    if extension != ".locked":
        print(f"{filename} is not a .locked file")
        return False

    original_path = os.path.join(directory, base_name)
    print(original_path)

    with open(original_path, 'wb') as f:
        f.write(decrypted)

    os.remove(filepath)
    print(f"Decrypted and unlocked {original_path}")

    return True