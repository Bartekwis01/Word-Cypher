import os
import sys
import json

DECODED_TEXT_PATH = 'decoded-text.txt'
CODED_TEXT_PATH = 'coded-text.txt'
DICTIONARY_PATH = 'dictionary.json'


def manual_run():
    if os.path.exists(DECODED_TEXT_PATH):
        print(
            f'{DECODED_TEXT_PATH} file detected. Please make sure that it is okay to overwrite that file. In case you '
            f'want to preserve that file, please close the program and move that file to another location.')
        input('Press Enter to continue, otherwise close the program.')
    if os.path.exists(CODED_TEXT_PATH):
        with open(CODED_TEXT_PATH, 'r', encoding='utf-8') as file:
            CODED_TEXT = file.read()
    else:
        print(
            f'ERROR - no coded file detected. Please move a file named {CODED_TEXT_PATH} into the same folder as the app '
            f'and run the program again')
        input('Press Enter to close...')
        sys.exit(2)
    if os.path.exists(DICTIONARY_PATH):
        with open(DICTIONARY_PATH, 'r', encoding='utf-8') as file:
            DICTIONARY = json.load(file)
    else:
        print(
            f'ERROR - no dictionary file detected. Please move a file named {DICTIONARY_PATH} into the same folder as the '
            f'app and run the program again. You can automatically generate one by coding a file using code.py program.')
        input(f'Press Enter to close...')
        sys.exit(2)
    decode(CODED_TEXT, DICTIONARY, DO_SAVE=True)


def decode(CODED_TEXT, DICTIONARY, DO_PRINT=True, DO_SAVE=False):
    word_not_found = False
    decoded_words = []
    DICTIONARY_KEYS = list(DICTIONARY.keys())
    DICTIONARY_VALUES = list(DICTIONARY.values())
    for word in CODED_TEXT.split():
        if word in DICTIONARY_VALUES:
            decoded_word = DICTIONARY_KEYS[DICTIONARY_VALUES.index(word)]
        else:
            decoded_word = 'NOT FOUND'  # The definition of the coded word was not found in the dictionary
            word_not_found = True
        decoded_words.append(decoded_word)
    decoded_text = ' '.join(decoded_words)
    if word_not_found and DO_PRINT:
        print(f'WARNING - at least one definition of a coded word was not found, it has been replaced with "|NOT '
              f'FOUND|" in the decoded text.')
    if DO_SAVE:
        with open(DECODED_TEXT_PATH, 'w', encoding='utf-8') as file:
            file.write(decoded_text)
    if DO_PRINT and DO_SAVE:
        print(f'Decoded text saved in {DECODED_TEXT_PATH}')
        input(f'Press Enter to exit...')
        sys.exit(0)
    return decoded_text


if __name__ == '__main__':
    manual_run()
