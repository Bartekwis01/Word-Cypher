import os
import sys
import json

DECODED_TEXT_PATH = 'decoded-text.txt'
TEXT_CODED_PATH = 'coded-text.txt'
DICTIONARY_PATH = 'dictionary.txt'

if os.path.exists(DECODED_TEXT_PATH):
    print(
        f'{DECODED_TEXT_PATH} file detected. Please make sure that it is okay to overwrite that file. In case you '
        f'want to preserve that file, please close the program and move that file to another location.')
    input('Press Enter to continue, otherwise close the program.')
if os.path.exists(TEXT_CODED_PATH):
    with open(TEXT_CODED_PATH, 'r', encoding='utf-8') as file:
        TEXT_CODED = file.read()
else:
    print(
        f'ERROR - no coded file detected. Please move a file named {TEXT_CODED_PATH} into the same folder as the app '
        f'and run the program again')
    input('Press Enter to close...')
    sys.exit(2)
if os.path.exists(DICTIONARY_PATH):
    with open(DICTIONARY_PATH, 'r', encoding='utf-8') as file:
        DICTIONARY = json.load(file)
        DICTIONARY_KEYS = list(DICTIONARY.keys())
        DICTIONARY_VALUES = list(DICTIONARY.values())
else:
    print(
        f'ERROR - no dictionary file detected. Please move a file named {DICTIONARY_PATH} into the same folder as the '
        f'app and run the program again. You can automatically generate one by coding a file using code.py program.')
    input(f'Press Enter to close...')
    sys.exit(2)


def decode():
    word_not_found = False
    text_decoded = ""
    for word in TEXT_CODED.split():
        if word in DICTIONARY_VALUES:
            word_decoded = DICTIONARY_KEYS[DICTIONARY_VALUES.index(word)]
        else:
            word_decoded = 'NOT FOUND' # The definition of the coded word was not found in the dictionary
            word_not_found = True
        text_decoded += word_decoded
        text_decoded += ' '

    if word_not_found:
        print(f'WARNING - at least one definition of a coded word was not found, it has been replaced with "|NOT '
              f'FOUND|" in the decoded text.')
    with open(DECODED_TEXT_PATH, 'w', encoding='utf-8') as file:
        file.write(text_decoded)
    print(f'Decoded text saved in {DECODED_TEXT_PATH}')
    input(f'Press Enter to exit...')
    sys.exit(0)


decode()


