#!/usr/bin/python3
"""
Defines a function that gives the dictionary description of simple data
structure for a JSON serialization of an object
"""


def class_to_json(obj):
    """Returns dictionary description of JSON serialization of object
    of simple data structures - list, dict, str, int and bool
    """
    obj_dict = {}
    for key, value in obj.__dict__.items():
        if type(value) in [int, str, bool]:
            obj_dict[key] = value
        elif type(value) == list:
            obj_dict[key] = [class_to_json(item) if hasattr(item, '__dict__')
                             else item for item in value]
        elif type(value) == dict:
            obj_dict[key] = {k: class_to_json(v) if hasattr(v, '__dict__')
                             else v for k, v in value.items()}
    return obj_dict
