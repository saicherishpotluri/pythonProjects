from dataclasses import replace


def replace_word():
    str = 'Hello, world. This is Cherish'
    print(str)
    words_to_replace = input("Enter the word to replace:")
    word_to_be_entered = input("Enter the word replacement:")
    print(str.replace(words_to_replace,word_to_be_entered))
replace_word()