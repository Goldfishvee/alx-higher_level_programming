#!/usr/bin/python3
"""
This is the "5-text_indentation" module.

This module supplies only  one argument, text_indentation(text).
It returns split string delimited by by the specified delimiters
"""



def text_indentation(text):
    """
    print text with 2 lines after encountering
    the characters ".,?:"
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    indent = False
    for char in text:
        if char in ['.', '?', ':']:
            print(char, end="\n\n")
            indent = True
        elif indent and char == " ":
            continue
        else:
            print(char, end="")
            indent = False
