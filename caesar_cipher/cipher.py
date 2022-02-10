from ast import Num
import nltk
from nltk.corpus import words, names
# below line used to the needed nltk packages  
# nltk.download()
words_list = words.words()
names_list = names.words()



def encrypt(text,key):
    encrypted_text = ''
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            encrypted_text += chr((ord(char) + key-65) % 26 + 65)
        # Encrypt lowercase characters
        elif (char.islower()):
            encrypted_text += chr((ord(char) + key-97) % 26 + 97)
        #encrypt whitespace spaces 
        elif char == ' ':
          encrypted_text += char
        else:
          encrypted_text += char
 
    return encrypted_text

def decrypt(encrypted, key):
  return encrypt(encrypted, -key)

def crack(encrypted):
    # create a loop to brute force the letter to get all options
    for i in range(26):
      # Create word count to use later 
        word_count = 0
        # encrypt the message based on the current loop
        words = encrypt(encrypted, i)
        # split each word into one word to check 
        list = words.split()
        # iterate through the words to check if they are in the names_list or words_list
        for text in list:
            if text in names_list or text.lower() in words_list:
              # if they are increase word_count by one
                word_count += 1
        # then check if the current word count is greater than 50% if so join all  the words together 
        if (word_count/len(list)) > .5:
            return " ".join(list)
    # if the word list count is not greater than 50% return just an empty string 
    return ""



if __name__ == '__main__':
  one = encrypt('Abc', 27)
  print(encrypt('apple', 27))
