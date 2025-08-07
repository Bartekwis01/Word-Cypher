import os
import sys
import random
import json

PLAINTEXT_PATH = 'plaintext.txt'
TEXT_ENCRYPTED_PATH = 'encrypted-text.txt'
DICTIONARY_PATH = 'dictionary.txt'
WORDS_PATH = 'words.txt'
WORDS = []

if os.path.exists(PLAINTEXT_PATH):
    with open(PLAINTEXT_PATH, 'r') as file:
        PLAINTEXT = file.read()
else:
    print(f'No plaintext file detected. Please create a file named {PLAINTEXT_PATH} and run the program again.')
    input('Press Enter to close...')
    sys.exit()
if os.path.exists(WORDS_PATH):
    with open(WORDS_PATH, 'r') as file:
        WORDS = []
        for line in file:
            word = line.strip()
            WORDS.append(word)
else:
    print(f'No words file detected. Please move a file named {WORDS_PATH} into the same folder as the app and run the program again. This is the file that is recommended: https://github.com/dwyl/english-words/blob/master/words_alpha.txt, but others may work provided that they are in the same format.')
    input('Press Enter to close...')
    sys.exit()
if os.path.exists(TEXT_ENCRYPTED_PATH):
    print(f'{TEXT_ENCRYPTED_PATH} file detected. Please make sure that it is okay to overwrite that file. In case you want to preserve that file, please close the program and move that file to another location, otherwise press Enter to continue...')
    input('Press Enter to continue, otherwise close the program.')
if os.path.exists(DICTIONARY_PATH):
    with open(DICTIONARY_PATH, 'r') as file:
        DICTIONARY = json.load(file)
else:
    print(f'WARNING - no dictionary file detected. The program will create a new one. This is normal when running the program for the first time.')
    input(f'Press Enter to acknowledge the warning and create a {DICTIONARY_PATH} file...')
    with open(DICTIONARY_PATH, 'w') as file:
        pass  # file created
    DICTIONARY = {}
with open(WORDS_PATH, 'r') as file:
    WORDS = []
    for line in file:
        word = line.strip()
        WORDS.append(word)

while True:
    MODE=str(input('Select mode. Type 1 to encrypt, type 2 to decrypt: '))
    if MODE == "1": #encrypt
        TEXT_ENCRYPTED = ""
        for word in PLAINTEXT.split():
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
    elif MODE == "2":
        pass
    else:
        print('Invalid mode. Please 1 to encrypt or 2 to decrypt: ')