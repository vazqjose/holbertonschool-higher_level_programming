#!/usr/bin/python3
''' Define class State that inherits from Base '''


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    ''' Defines a State from table states '''

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
