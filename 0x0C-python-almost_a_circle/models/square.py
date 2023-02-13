#!/usr/bin/python3
"""Define child class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize Square and its associated propertie
        
        Args:
            size (int): size of Square
            x (int): x dimensonal value of Square
            y (int): y dimensional value of Square
            id (int): instance id of Square
        Return:
            raise TypeError if attribute is not an integer
            raise ValueError if attribute is less than or equal to zero
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """set/get the size of Square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates and assigns new attributes to Square
        
        Args:
            *args (ints): new list of arguments (no-keyword-argument)
            1st arg (int): id attribute of Square
            2nd arg (int): size attribute of Square
            3rd arg (int): x attribute of Square
            4th arg (int): y attribute of Square
            **kwargs (dict): New key/value argument
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return dict representation of Square"""
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}

    def __str__(self):
        """informal string representation of objects in Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
