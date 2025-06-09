# Creating , Viewing, and Managing Entries

from cryptography.fernet import Fernet

import os
from datetime import datetime

def create_entry():
    title = input("Enter the title of your diary entry: ")
    content = input("Enter your diary content: ")
    date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    # Encrypt content 
    encrypt_content = encrypt_text(content)

    # Save entry
    file_name = f"{date}_{title}.txt"
    with open(os.path.join("entries", file_name), "wb") as file:
        file.write(encrypt_content)
    print(f"Diary entry '{title}' saved successfully!")

def list_entries():
    entries = os.listdir("entries")
    if entries:
        print("Your Diary Entries: ")
        for index, entry in enumerate(entries, start=1):
            print(f"{index}. {entry}")
    else:
        print("No diary entries found.")

def read_entry():
    list_entries()
    file_name = input("Enter the name of the entry to read: ")
    file_path = os.path.join("entries", file_name)

    try:
        with open(file_path, "rb") as file:
            encrypted_content = file.read()
        content = decrypt_text(encrypted_content)
        print("\nDiary Entry Content: ")
        print(content)
    except FileNotFoundError:
        print("Entry not Found.")








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