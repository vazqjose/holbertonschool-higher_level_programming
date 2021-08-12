#!/usr/bin/python3
"""
Write a script that prints the State object with the name passed as argument
    - Your script should take 3 arguments: mysql username, mysql
        password and database name
    - You must use the module SQLAlchemy
    - You must import State and Base from model_state - from
        model_state import Base, State
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
    myState = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        user, passwd, dbname), pool_pre_ping=True)

    Session = sessionmaker(engine)
    mySession = Session()

    numRows = mySession.query(State).filter_by(name=myState).count()
    results = mySession.query(State).filter_by(name=myState)

    if numRows == 0:
        print("Not found")
    else:
        for state in results:
            print("{}".format(state.id))
