#!/usr/bin/python3
''' Define class City that inherits from Base '''


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class City(State):
    ''' Defines a State from table cities '''

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer, FK(State.id, nullable=False))
