#!/usr/bin/python3
''' Create the state model from table states '''


from sqlalchemy import create_engine, sessionmaker
from states import State

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://root:root@localhost/hbtn_0e_6_usa")

    Session = sessionmaker(engine)
    session = Session()

    states = session.query(State).order_by(State.id)

    for state in states:
        print(state.name)
