#!/usr/bin/python3
"""Decodes a JSON string representation into Python"""

import json


def from_json_string(my_str):
    """Decodes py data structure represented by a JSON string

    Args:
        my_str(str): JSON object to decode
    """
    return json.loads(my_str)
