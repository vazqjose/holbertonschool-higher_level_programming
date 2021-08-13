#!/usr/bin/python3
'''
Link class to table Cities
'''


import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        user, passwd, dbname), pool_pre_ping=True)

    Session = sessionmaker(engine)
    mySession = Session()

    query = session.query(State, City).join(City)

    for state, city in query.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
