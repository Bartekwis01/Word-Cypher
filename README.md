# Word Cypher

This is a simple tool that allows you to code and decode an (almost) unlimited length of text(the limitation is the
amount of words in the words.json file*). It works by switching out one word for another and storing the
dictionary([codebook](https://en.wikipedia.org/wiki/Codebook)) in a file. For example: "cat" can be coded into "dog"
and "dog" can be then decoded back into "cat" with the dictionary:
"cat": "dog". This program currently preserves cases, punctuation marks and emojis.

## Warning

This program has been made for **educational purposes only**. It is no way a viable solution to secure any important
data. While it is more secure than a substitution cipher, this program is still massively **vulnerable** to attacks such
as word [frequency analysis](https://en.wikipedia.org/wiki/Frequency_analysis). Another drawback is that this method
relies on a single dictionary to both code and decode data, therefore its dictionary is
a [symmetrical key](https://en.wikipedia.org/wiki/Symmetric-key_algorithm), which **cannot be sent securely over an
untrusted media**. To learn more I recommend reading [this article](https://en.wikipedia.org/wiki/Code_(cryptography))
on Wikipedia. In summary, **this program codes rather than encrypts data**.

## How to use in your program

A quick guide to use code and decode functions in your program.

### Importing

Using the functions is quite straightforward. First you should import code and/or decode function using
`from code import code` and/or `from decode import decode`.

### code()

#### PARAMETERS

The `code()` function only needs `PLAINTEXT` parameter, but you can provide four more;

`PLAINTEXT` - Accepts a string that needs to be coded.

`DICTIONARY` - By default will create a new dictionary and overwrite any existing one if `DO_SAVE==True`. It is
recommended to provide an existing dictionary in standard dictionary format.

`WORDS` - By default will try to use a words.json file situated in the same directory as the program, the program will
exit with code 2 if it doesn't find it. Accepts any string with one word per line.

`DO_PRINT` - By default the program will not print anything to console, but it can be changed by setting this to `True`

`DO_SAVE` - By default the program will only output coded text and the dictionary, but when this setting is set to
`True` the program will additionally create files named *coded-text.txt* and *dictionary.json* with the corresponding
values in the working directory of the program.

#### OUTPUT

The `code()` function outputs two things:

- Coded text as a standard string
- Dictionary as a standard dictionary

To pipe both into a corresponding variable and dictionary simply use:  
`coded_text, dict = code('Example string to code')`

### decode()

#### PARAMETERS

The `decode()` function only needs `CODED_TEXT` and `DICTIONARY` parameters, but you can provide 2 more;

`CODED_TEXT` - Accepts a string that needs to be decoded.

`DICTIONARY` - Accepts a dictionary that contains the definitions of coded words.

`DO_PRINT` - By default the program will not print anything to console, but it can be changed by setting this to `True`.

`DO_SAVE` - By default the program will only output decoded text, but when this setting is set to `True` the program
will additionally create a file named `decoded-text.txt` that will contain the decoded text.

#### OUTPUT

The `decode()` function simply outputs the decoded text as a single string.

## How does it work?

A not so short explanation of the way this program works. I will focus on the core method and not the supporting
mechanisms.

### Coding - code.py

The program loops through each word and checks if it is already present in the dictionary, if so the corresponding word
is added to the list of words, if it isn't then the program randomly selects a word from the words.json file that is not
present in the dictionary and uses that as the coded word that's added to the list of words. At the end it joins each
word with a space and returns the result.

### Decoding - decode.py

The program loops through each coded word and checks if it's definition is in the dictionary, if so it writes the
definition to the list of decoded words, otherwise it writes |NOT FOUND| in the place of it. At the end it joins each
word with a space and returns the result.

### Testing - validator.py

The program imports code and decode functions from the corresponding files and uses them to first encrypt then decrypt
some text(first *Hello World!* then emojis, then numbers, then polish characters). After that it checks if the decoded
text is the same as the plaintext used for generating the coded text and prints the result.

### Not so intended but I won't fix it behaviour

The program considers a word to be an unlimited-length of characters from space to space. Because of that dots and
commas etc. are saved with the word before them so that *hello!* and *hello?* are considered different words and groups
of emojis are saved as a single word in the dictionary. This makes it harder to break the cypher, but also is less
intuitive.