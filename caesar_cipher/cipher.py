from ast import Num
import nltk
from nltk.corpus import words, names
# below line used to the needed nltk packages  
# nltk.download()


def encrypt(text,key):
    encrypted_text = ''
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            encrypted_text += chr((ord(char) + key-65) % 26 + 65)
        #encrypt whitespace spaces 
        elif char == ' ':
          encrypted_text += char
        # Encrypt lowercase characters
        elif (char.islower()):
            encrypted_text += chr((ord(char) + key-97) % 26 + 97)
        else:
          encrypted_text += char
 
    return encrypted_text

def decrypt(encrypted, key):
  return encrypt(encrypted, -key)

def crack(encrypted):
  pass


if __name__ == '__main__':
  one = encrypt('Abc', 2)
  assert one == 'Cde'
  two = decrypt(one, 2)
  assert two == 'Abc'
