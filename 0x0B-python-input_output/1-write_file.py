#!/usr/bin/python3
"""Define a function that writes to a file, returns number of chars written"""


def write_file(filename="", text=""):
    """write content to a file
    
    Args:
        filename(str): name of file to write to
        text(str): string chars to write to file
    
    Return:
        count of chars written.
        function will create file if it doesn't exist
        function will overwirte content of file, ifit already exists
    """
    with open(filename, 'w', encoding='UTF-8') as f:
        return f.write(text)
