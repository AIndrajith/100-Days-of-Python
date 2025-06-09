# write decrypt and encrypt functions

from cryptography.fernet import Fernet

# Generate and save a key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load the key
def Load_key():
    return open("secret.key", "rb").read()

# Encrypt text
def encrypt_text(text):
    key = Load_key()
    cipher = Fernet(key)
    return cipher.encrypt(text.encode())

# Decrypt text 
def decrypt_text(encrypted_text):
    key = Load_key()
    cipher = Fernet(key)
    return cipher.decrypt(encrypt_text).decode()