# Script Name:                  Class 16
# Author:                       Zachariah Woodbridge
# Date of latest revision:      29 Jan 2024
# Purpose:                      Python script that prompts the user to do an offensive, Dictionary Iterator
# Disclaimer:                   This script was written with the assistance of codeium.

# Declaration of imports
import nltk
import ssl
from nltk.corpus import words
# Declaration of variables

# Declaration of functions
try:
   _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
   pass
else:
   ssl.create_default_https_context = _create_unverified_https_context

# Download the 'words' dataset from the NLTK library and return the list of words.
def get_words():
   nltk.download('words')
   word_list = words.words()
   return word_list

# Check if a word is in the given list of words.
def check_for_word(words):
   user_answer = input("Enter a word: ")
   if user_answer in words:
       print(f"{user_answer} is in the dictionary")
   else:
       print(f"{user_answer} is not in your wordlist")

           if not line:
           if not line:

# Function to load an external file and store its contents in a list.
def load_external_file():
   password_list = []
   with open('rockyou.txt', 'r') as file:
       while True:
           line = file.readline()
           if not line:
               break
           line = line.rstrip()
           password_list.append(line)
           print(password_list)

# Main       
if __name__ == "__main__":
   nexternal_words = get_words()
   check_for_word(nexternal_words)
   load_external_file()

# End

# End
