#!/usr/bin/python3
"""Define class Base"""

import json
import csv
import turtle


class Base:
    """creates a Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize base class

        Args:
            id (int): id of object instances created
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list dictionaries

        Args:
            list_dictionaries (list): list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file

        Args:
            list_objs (list): list of instances that inherit from Base
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as jf:
            if list_objs is None:
                jf.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                jf.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of JSON str repr of json_string

        Args:
            json_string (str): string representation of a list of dicts
        """

        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns a class from a dict of attributes

        Args:
            **dictionary (dict): key/value pairs of attr to initialize
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_attr = cls(1, 1)
            else:
                new_attr = cls(1)
            new_attr.update(**dictionary)
            return new_attr

    @classmethod
    def load_from_file(cls):
        """Returns a list of classes instantiated from a file of JSON strs
           File is read from <cls.__name__>.json
        Return:
            if file does not exist - an empty list
            Else - a list of instantiated classes
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, 'r') as jf:
                list_dicts = Base.from_json_string(jf.read())
                return [cls.create(**items) for items in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serialize objects in CSV

        Args:
            list_objs (obj): list of inherited Base instances to serialize
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of classes instantiated from a CSV file
        File is read from <cls.__name__>.csv
        Return:
            if file does not exist - an empty list
            Else - a list of instantiated classes
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r', newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
