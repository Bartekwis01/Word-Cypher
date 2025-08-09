from code import code
from decode import decode

def hello_world(debug=False):
    text = 'Hello World!'
    coded, dictionary = code(text)
    decoded = decode(coded, dictionary)
    if text == decoded:
        print('OK - emojis')
    else:
        print('ERROR - emojis')
        if debug:
            print(f' TEXT: {text}\n CODED TEXT: {coded} \n DECODED TEXT: {decoded} \n DICTIONARY: {dictionary}')


def emojis(debug=False):
    text = '👍💵🟪🟩💀🌩️💕😘😒😊😂🤣✌️🤞😉🤷‍♂️🤷‍♀️🤦‍♂️🤩😎😁'
    coded, dictionary = code(text)
    decoded = decode(coded, dictionary)
    if text == decoded:
        print('OK - emojis')
    else:
        print('ERROR - emojis')
        if debug:
            print(f' TEXT: {text}\n CODED TEXT: {coded} \n DECODED TEXT: {decoded} \n DICTIONARY: {dictionary}')


def numbers(debug=False):
    text = '0123456789'
    coded, dictionary = code(text)
    decoded = decode(coded, dictionary)
    if text == decoded:
        print('OK - numbers')
    else:
        print('ERROR - numbers')
        if debug:
            print(f' TEXT: {text}\n CODED TEXT: {coded} \n DECODED TEXT: {decoded} \n DICTIONARY: {dictionary}')


def polish_characters(debug=False):
    text = 'ęóąśłżźćń'
    coded, dictionary = code(text)
    decoded = decode(coded, dictionary)
    if text == decoded:
        print('OK - polish characters')
    else:
        print('ERROR - polish characters')
        if debug:
            print(f' TEXT: {text}\n CODED TEXT: {coded} \n DECODED TEXT: {decoded} \n DICTIONARY: {dictionary}')


def plaintext(debug=False):
    with open('plaintext.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    coded, dictionary = code(text)
    decoded = decode(coded, dictionary)
    if text == decoded:
        print('OK - plaintext')
    else:
        print('ERROR - plaintext')
        if debug:
            print(f' TEXT: {text}\n CODED TEXT: {coded} \n DECODED TEXT: {decoded} \n DICTIONARY: {dictionary}')


if __name__ == '__main__':
    hello_world(True)
    emojis(True)
    numbers(True)
    polish_characters(True)
    plaintext(True)
