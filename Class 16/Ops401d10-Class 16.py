# Script Name:                  Class 16
# Author:                       Zachariah Woodbridge
# Date of latest revision:      29 Jan 2024
# Purpose:                      Python script that prompts the user to do an offensive, Dictionary Iterator
# Disclaimer:                   This script was written with the assistance of codeium.

import nltk
from nltk.corpus import words

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
def load_external_file():
   password_list = []
   with open('/home/rockyou-test.txt', 'r') as file:
       for line in file:
           line = line.strip()  # Remove leading/trailing whitespace
           password_list.append(line)
   return password_list

# Main      
if __name__ == "__main__":
   word_list = get_words()  # Download the words dataset
   load_external_file()  # Load the external file
   check_for_word(word_list)  # Check for a word in the word list