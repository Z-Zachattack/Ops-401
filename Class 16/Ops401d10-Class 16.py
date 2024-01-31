# Script Name:                  Class 16
# Author:                       Zachariah Woodbridge
# Date of latest revision:      29 Jan 2024
# Purpose:                      Python script that prompts the user to do an offensive, Dictionary Iterator
# Disclaimer:                   This script was written with the assistance of codeium.

import os
import nltk
from nltk.corpus import words
import time

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

# Function to load an external file and store its contents in a list.
def load_external_file(filepath):
  password_list = []
  with open(filepath, 'r') as file:
      for line in file:
          line = line.strip()  # Remove leading/trailing whitespace
          password_list.append(line)
  return password_list

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

def defensive(filepath):
   word_list = get_words()  # Download the words dataset
   load_external_file(filepath)  # Load the external file
   check_for_word(word_list)  # Check for a word in the word list
# Main     
def main():
   filepath = pw_filepath()
   # Print menu
   print("Select a mode:")
   print("Mode 1: Offensive; Dictionary Iterator")
   print("Mode 2: Defensive; Password Recognized")
   mode = input("Enter the mode number (1, or 2): ")
   if mode == "1":
       offensive(filepath)
   elif mode == "2":
       defensive(filepath)
# Call the main function
if __name__ == "__main__":
   main()
# End
