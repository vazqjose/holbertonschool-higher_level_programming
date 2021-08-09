#!/usr/bin/python3
"""
Write a script that lists all State objects from the database
    - Your script should take 3 arguments: mysql username,
      mysql password and database name
    - You must use the module SQLAlchemy
    - You must import State and Base from model_state - from
      model_state import Base, State
    - Your script should connect to a MySQL server running on
      localhost at port 3306
    - Results must be sorted in ascending order by states.id
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
