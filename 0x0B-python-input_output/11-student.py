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

    def to_json(self, attrs=None):
        """Retrieves dict repr of Student instance
        
        Args:
            attrs(any): attribute types to retrieve
        
        Return:
            all attribute values except if attribute is str
            then return only attribute names
        """
        if attrs is None:
            return self.__dict__
        filtered_dict = {}
        for item in attrs:
            try:
                filtered_dict[item] = self.__dict__[item]
            except FileNotFoundError:
                pass
        return filtered_dict

    def reload_from_json(self, json):
        """replace all attributes of Student class
        
        Args:
            json(obj): JSON dict object
        """
        for key in json:
            try:
                setattr(self, key, json[key])
            except FileNotFoundError:
                pass
