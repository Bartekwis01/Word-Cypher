import os
import sys
import json

PLAINTEXT_PATH = 'plaintext.txt'
TEXT_ENCRYPTED_PATH = 'encrypted-text.txt'
DICTIONARY_PATH = 'dictionary.txt'

if os.path.exists(PLAINTEXT_PATH):
    print(
        f'{PLAINTEXT_PATH} file detected. Please make sure that it is okay to overwrite that file. In case you want to preserve that file, please close the program and move that file to another location.')
    input('Press Enter to continue, otherwise close the program.')
    with open('plaintext.txt', 'r') as file:
        PLAINTEXT = file.read()
if not os.path.exists(TEXT_ENCRYPTED_PATH):
    print(
        f'ERROR - no encrypted file detected. Please move a file named {TEXT_ENCRYPTED_PATH} into the same folder as the app and run the program again')
    input('Press Enter to close...')
    sys.exit()
if os.path.exists(DICTIONARY_PATH):
    with open(DICTIONARY_PATH, 'r') as file:
        DICTIONARY = json.load(file)
else:
    print(
        f'ERROR - no dictionary file detected. Please move a file named {DICTIONARY_PATH} into the same folder as the app and run the program again. You can automatically generate one by encrypting a file using encrypt.py program.')
    input(f'Press Enter to close...')
    sys.exit()


def decrypt():
    pass  # to be implemented
