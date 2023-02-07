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
        if isinstance(attrs, list) and all(isinstance(item, str)
                                           for item in attrs):
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        return self.__dict__
