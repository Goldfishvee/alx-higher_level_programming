#!/usr/bin/python3
"""Define a function that adds a string to the end of a file"""


def append_write(filename="", text=""):
    """Add string at the end of a text file and return count of chars added
    Args:
        filename(str): name of file to write to
        text(str): string chars to write to file
    Return:
        count of chars written.
        function will create file if it doesn't exist
    """
    with open(filename, 'a', encoding='UTF-8') as f:
        return f.write(text)
