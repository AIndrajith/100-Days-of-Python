import os
import getpass
from datetime import datetime
from cryptography.fernet import Fernet

# Encryption setup

# Generate and save a key
def generate_key():
    if not os.path.exists("secret.key"):
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

# Diary Functions

def create_entry():
    title = input("Enter the title of your diary entry: ")
    content = input("Enter your diary content: ")
    date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    # Encrypt content 
    encrypt_content = encrypt_text(content)

    os.makedirs("entries", exist_ok=True)

    # Save entry
    file_name = f"{date}_{title}.txt"
    with open(os.path.join("entries", file_name), "wb") as file:
        file.write(encrypt_content)
    print(f"Diary entry '{title}' saved successfully!")

def list_entries():
    os.makedirs("entries", exist_ok=True)
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
        
# Authentication

def authenticate():
    correct_password = "mypassword" # set your password here
    password = getpass.getpass("Enter your password: ")
    if password == correct_password:
        print("Access Granted!")
        return True
    else:
        print("Access Denied!")
        return False
    
# Main app
def main():
    generate_key()
    if authenticate():
        while True:
            print("\nOptions: ")
            print("1. Create a New Entry")
            print("2. View All Entries")
            print("3. Read an Entry")
            print("4. Exit")
            choice = input("Enter your choice : ")
            if choice == "1":
                create_entry()
            elif choice == "2":
                list_entries()
            elif choice == "3":
                read_entry()
            elif choice == "4":
                print("Good bye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()