#!/usr/bin/python3
"""Define a function that reads a file and prints content to stdout"""


def read_file(filename=""):
    """read a file and print contents to stdout"""
    with open(filename, 'r', encoding="UTF-8") as f:
        read_data = f.read()
        print(read_data, end="")
