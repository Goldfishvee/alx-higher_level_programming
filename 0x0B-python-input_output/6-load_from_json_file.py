#!/usr/bin/python3
"""Defines a function that creates an object from a JSON file"""

import json


def load_from_json_file(filename):
    """create an object from a JSON file
    
    Args:
        filename(str): name of file to create object from
    
    Return:
        contents of created object file
    """
    with open(filename, 'r') as f:
        return json.load(f)
