#!/usr/bin/python3
"""
Create a db schema using SQLAlchemy
The script will create a class definition of State and an instance
'Base = declarative_base()'
Establish relationship with class attribute 'cities' of class City
If State obj is deleted, all linked City objs must also be automatically deld
Reference from a City obj to its State should be named 'state'
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

stateMeta = MetaData()  # parameterize metadata for modular use

Base = declarative_base(metadata=stateMeta)  # create Base instance


class State(Base):
    """Creates an instance of State

    Args:
        id(int): id of state
        name(str): name of state
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False,
                unique=True)
    name = Column(String(128), nullable=False)

    cities = relationship('City', cascade='all, delete', backref='states')
