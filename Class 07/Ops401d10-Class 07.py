#!/usr/bin/env python3

# Script Name:                  Class 07
# Author:                       Zachariah Woodbridge
# Date of latest revision:      17 Jan 2024
# Purpose:                      Python script that Encrypts/Decrypts files and messages. Added Encrypting/Decrypting folders recursively
# Disclaimer:                   This script was written with the assistance of codeium.

# Declaration of imports
from cryptography.fernet import Fernet
import os

# Declaration of variables

# Declaration of functions
# This function will generate a Fernet key.
def generate_key():
    return Fernet.generate_key()

# This function will load the Fernet key.
def load_key():
    return open("secret.key", "rb").read()

# This function will save the Fernet key.
def save_key(key):
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# This function will encrypt a file.
def encrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        data = file.read()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    with open(file_path + ".enc", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

# This function will decrypt a file.
def decrypt_file(file_path, key):
    with open(file_path, "rb") as encrypted_file:
        data = encrypted_file.read()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(data)
    with open(file_path[:-4], "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

# This function will encrypt a message.
def encrypt_message(message, key):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    print("Encrypted Message:", encrypted_message.decode())

# This function will decrypt a message.
def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message.encode())
    print("Decrypted Message:", decrypted_message.decode())

# Function to recursively encrypt a folder and its contents
def encrypt_folder(folder_path, key):
    fernet = Fernet(key)
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith(".txt"):
                encrypt_file(file_path, key)
    print("Encrypted Folder")

# Function to recursively decrypt an encrypted folder and its contents
def decrypt_folder(folder_path, key):
    fernet = Fernet(key)
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith(".enc"):
                decrypt_file(file_path, key)
    print("Decrypted Folder")

# Main
def main():
    if not os.path.isfile("secret.key"):
        key = generate_key()
        save_key(key)
    else:
        key = load_key()

    mode = int(input("Select mode (Mode 1-6):\n 1: Encrypt file\n 2: Decrypt file\n 3: Encrypt message\n 4: Decrypt message\n 5: Encrypt Folder - Recursively\n 6: Decrypt Folder - Recursively\n Choose With Number: "))

    if mode in [1, 2]:
        file_path = input("Enter file path: ")

        if mode == 1:
            encrypt_file(file_path, key)
            print("Encryption successful")

        elif mode == 2:
            decrypt_file(file_path, key)
            print("Decryption successful")

    elif mode == 3:
        message = input("Enter message to be encrypted: ")
        encrypt_message(message, key)

    elif mode == 4:
        encrypted_message = input("Enter encrypted message to be decrypted: ")
        decrypt_message(encrypted_message, key)
    
    elif mode == 5:
        # Prompt user for the folder path
        folder_path = input("Enter the folder path: ")

        # Recursively encrypt the folder and its contents
        encrypt_folder(folder_path, key)

    elif mode == 6:
        # Prompt user for the folder path
        folder_path = input("Enter the folder path: ")

        # Recursively decrypt the encrypted folder and its contents
        decrypt_folder(folder_path, key)
    else:
        print("Invalid mode selected.")
# End
if __name__ == "__main__":
    main()
