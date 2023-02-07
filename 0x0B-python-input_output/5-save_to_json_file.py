#!/usr/bin/python3
"""Writes an Object to a text using JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """write an object to text file using JSON representation

    Args:
        my_obj(str): object to write to file
        filename(str): name of file to write object to
    """
    with open(filename, 'w') as f:
        return json.dump(my_obj, f)
