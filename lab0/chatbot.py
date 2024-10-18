import ssl
#
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

import nltk


def process(user_input):
    tokens = nltk.word_tokenize(user_input)
    return tokens


def main():
    while True:
        user_input = input("You : ")
        if user_input.lower() == 'exit':
            print("Goodbye !")
            break
        processed_input = process(user_input)
        print(f"Bot : You said {processed_input}")


if __name__ == " __main__ ":
    main()
