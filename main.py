import os
import sys
import random
import json
TEXT_TO_ENCRYPT_PATH = 'plaintext.txt'
TEXT_ENCRYPTED_PATH = 'encrypted-text.txt'
DICTIONARY_PATH = 'dictionary.txt'
WORDS_PATH = 'words.txt'
WORDS = []
if not os.path.exists(TEXT_TO_ENCRYPT_PATH):
    print(f'No plaintext file detected. Please create a file named {TEXT_TO_ENCRYPT_PATH} and run the program again.')
    input('Press Enter to close...')
    sys.exit()
if not os.path.exists(WORDS_PATH):
    print(f'No words file detected. Please move a file named {WORDS_PATH} into the same folder as the app and run the program again. This is the file that is recommended: https://github.com/dwyl/english-words/blob/master/words_alpha.txt, but others may work provided that they are in the same format.')
    input('Press Enter to close...')
    sys.exit()
if os.path.exists(TEXT_ENCRYPTED_PATH):
    print(f'{TEXT_ENCRYPTED_PATH} file detected. Please make sure that it is okay to overwrite that file. In case you want to preserve that file, please close the program and move that file to another location, otherwise press Enter to continue...')
    input('Press Enter to continue, otherwise close the program.')
if not os.path.exists(DICTIONARY_PATH):
    print(f'WARNING - no dictionary file detected. The program may only encrypt a message (this is normal when running the program for the first time).')
    input('Press Enter to acknowledge the warning and create a {DICTIONARY_PATH} file...')
    with open(DICTIONARY_PATH, 'w') as file:
        pass
else:
    with open(DICTIONARY_PATH, 'r') as file:
        DICTIONARY = {}
        DICTIONARY = json.load(file)
with open(TEXT_TO_ENCRYPT_PATH, 'r') as file:
    TEXT_TO_ENCRYPT = file.read()
with open(WORDS_PATH, 'r') as file:
    WORDS = []
    for line in file:
        word = line.strip()
        WORDS.append(word)

while True:
    MODE=str(input('Select mode. Type 1 to encrypt, type 2 to decrypt: '))
    if MODE == "1" or MODE == "2":
        break
    else:
        continue
print(DICTIONARY)
if MODE == "1": #encrypt
    TEXT_ENCRYPTED = ""
    for word in TEXT_TO_ENCRYPT.split():
        if word in DICTIONARY.keys(): #.keys()
            ENCRYPTED_WORD = DICTIONARY[word]
        else:
            while True:
                random_word = WORDS[random.randint(0, len(WORDS)-1)]
                if random_word in DICTIONARY:
                    continue
                else:
                    break
            ENCRYPTED_WORD = random_word
        TEXT_ENCRYPTED += ENCRYPTED_WORD
        TEXT_ENCRYPTED += " "
        DICTIONARY.update({word: ENCRYPTED_WORD})
    with open(TEXT_ENCRYPTED_PATH, 'w') as file:
        file.write(TEXT_ENCRYPTED)