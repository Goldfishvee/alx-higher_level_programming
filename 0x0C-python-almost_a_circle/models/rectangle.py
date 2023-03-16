#!/usr/bin/python3
"""Define child class Rectangle"""

from models.base import Base


class Rectangle(Base):
    """Defines a Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize Rectangle

        Args:
            width (int): width dimension of Rectangle
            height (int): height dimension of Rectangle
            x (int): cartesian coordinate x of Rectangle
            y (int): cartesian coordinate y of Rectangle
            id (int): id of Rectangle
        Return:
            raise TypeError if attribute is not an integer
            raise ValueError if attribute is less than or equal to zero
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """set width dimension of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """set height dimension of Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """set x coordinate of Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """set y coordinate of Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Print Rectangle to stdout using #"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for char in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Updates the Rectangle

        Args:
            args (int): aggregates and displays all arguments given to func
            1st arg (int): id attribute
            2nd arg (int): width attribute
            3rd arg (int): height attribute
            4th arg (int): x attribute
            5th arg (int): y attribute
            kwargs (dict): assigns a key/value argument to attributes
        *args is a 'no-keyword' argument where arg order is important
        **kwargs is a 'key-worded argument' where arg order is not important
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of Rectangle"""
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}

    def __str__(self):
        """canonical string representation of object Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)
