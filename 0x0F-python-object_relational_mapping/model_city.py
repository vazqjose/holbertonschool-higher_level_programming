#!/usr/bin/python3
''' Defines class City that inherits from
Base '''


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import State, Base

Base = declarative_base()


class City(Base):
    ''' Defines a City '''

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
