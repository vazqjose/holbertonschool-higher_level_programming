#!/usr/bin/python3
"""
List all State objects that contain the letter 'a'
    - Your script should take 3 arguments: mysql username, mysql
        password and database name
    - You must use the module SQLAlchemy
    - You must import State and Base from model_state - from
        model_state import Base, State
    - The state you display must be the first in states.id
    - You are not allowed to fetch all states from the database
        before displaying the result
    - Your code should not be executed when imported
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        user, passwd, dbname), pool_pre_ping=True)

    Session = sessionmaker(engine)
    mySession = Session()

    statesWithA = mySession.query(State).filter(State.name.like('%a%'))

    for state in statesWithA:
        print("{}: {}".format(state.id, state.name))
