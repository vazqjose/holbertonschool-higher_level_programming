#!/usr/bin/python3
"""
Write a python file that contains the class definition of a
State and an instance Base = declarative_base():

    State class:
    - inherits from Base
    - links to the MySQL table states
    - class attribute id that represents a column of an
      auto-generated, unique integer, can’t be null and is a primary key
    - class attribute name that represents a column of a string with
      maximum 128 characters and can’t be null
"""


from sqlalquemy.ext.declarative import declarative_base
from sqlalquemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
        State class of the table states inherited from Base
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
