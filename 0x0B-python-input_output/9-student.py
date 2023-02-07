#!/usr/bin/python3
"""
Defines a class Student with JSON dict representation
"""


class Student():
    """Define a Student"""
    def __init__(self, first_name, last_name, age):
        """initialize Student
        
        Args:
            first_name(str): first name of student
            last_name(str): last name of student
            age(int): age of student
        
        Return:
            dict representation of attributes of Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dict repr of Student instance"""
        obj_dict = {}
        for key, value in self.__dict__.items():
            if type(value) in [str, int, bool]:
                obj_dict[key] = value
            elif type(value) == list:
                obj_dict[key] = [class_to_json(item)
                                 if hasattr(item, '__dict__')
                                 else item for item in value]
            elif type(value) == dict:
                obj_dict[key] = {k: class_to_json(v) if hasattr(v, '__dict__')
                                 else v for k, v in value.items()}
        return obj_dict
