#!/usr/bin/python3
"""Function that splits a text according to ., ?, and :"""


def text_indentation(text):
    """function that splits a string of text

    Arguments:
        text (str): the string of text to split
    """

    if type(text) != str:
        raise TypeError("text must be a string")
    i = 0
    text = text.strip()

    while i < len(text):
        print(text[i], end='')
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print('\n')
            if i == len(text) - 1:
                break
            if text[i + 1] == ' ':
                i = i + 1
            while text[i] == ' ' and text[i + 1] == ' ':
                i = i + 1
        i = i + 1
