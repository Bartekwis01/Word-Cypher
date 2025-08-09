import os
import sys
import random
import json

PLAINTEXT_PATH = 'plaintext.txt'
CODED_TEXT_PATH = 'coded-text.txt'
DICTIONARY_PATH = 'dictionary.json'
WORDS_PATH = 'words.json'
WORDS = []


def manual_run(DO_PRINT, DO_SAVE):
    if os.path.exists(PLAINTEXT_PATH):
        with open(PLAINTEXT_PATH, 'r', encoding='utf-8') as file:
            PLAINTEXT = file.read()
    else:
        print(f'No plaintext file detected. Please create a file named {PLAINTEXT_PATH} and run the program again.')
        input('Press Enter to close...')
        sys.exit(2)
    if os.path.exists(CODED_TEXT_PATH):
        print(f'{CODED_TEXT_PATH} file detected. Please make sure that it is okay to overwrite that file. In case you '
              f'want to preserve that file, please close the program and move that file to another location, '
              f'otherwise press Enter to continue...')
        input('Press Enter to continue, otherwise close the program.')
    if os.path.exists(DICTIONARY_PATH):
        with open(DICTIONARY_PATH, 'r', encoding='utf-8') as file:
            DICTIONARY = json.load(file)
    else:
        print(
            f'WARNING - no dictionary file detected. The program will create a new one. This is normal when running the '
            f'program for the first time.')
        input(f'Press Enter to acknowledge the warning and create a {DICTIONARY_PATH} file...')
        # noinspection PyRedeclaration
        DICTIONARY = {}
    code(PLAINTEXT, DICTIONARY, DO_PRINT=DO_PRINT, DO_SAVE=DO_SAVE)


def read_words(DO_PRINT):
    if os.path.exists(WORDS_PATH):
        with open(WORDS_PATH, 'r', encoding='utf-8') as file:
            WORDS = list(json.load(file).keys())
        return WORDS
    else:
        if DO_PRINT:
            print(
                f'No words file detected. Please move a file named {WORDS_PATH} into the same folder as the app and run the '
                f'program again. This is the file that is recommended: '
                f'https://github.com/dwyl/english-words/blob/master/words_alpha.txt, but others may work provided that they '
                f'are in the same format.')
            input('Press Enter to close...')
        sys.exit(2)


def code(PLAINTEXT, DICTIONARY=None, WORDS=None, DO_PRINT=False, DO_SAVE=False):
    if DICTIONARY is None:
        DICTIONARY = {}
    if WORDS is None:
        WORDS = read_words(DO_PRINT)
    coded_words = []
    for word in PLAINTEXT.split():
        if word in DICTIONARY.keys():  # .keys()
            coded_word = DICTIONARY[word]
        else:
            while True:
                random_word = WORDS[random.randint(0, len(WORDS) - 1)]
                if random_word in DICTIONARY:
                    continue
                else:
                    break
            coded_word = random_word
        DICTIONARY.update({word: coded_word})
        coded_words.append(coded_word)
    coded_text = ' '.join(coded_words)
    if DO_SAVE:
        with open(CODED_TEXT_PATH, 'w', encoding='utf-8') as file:
            file.write(coded_text)
        with open(DICTIONARY_PATH, 'w', encoding='utf-8') as file:
            json.dump(DICTIONARY, file, ensure_ascii=False)
    if DO_PRINT and DO_SAVE:
        print(f'Coded text saved in {CODED_TEXT_PATH}')
        input('Press Enter to continue...')
        sys.exit(0)
    return coded_text, DICTIONARY


if __name__ == '__main__':
    manual_run(DO_PRINT=True, DO_SAVE=True)
