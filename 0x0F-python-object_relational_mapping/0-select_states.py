#!/usr/bin/python3
"""
Write a script that lists all states from the database hbtn_0e_0_usa:
    - Your script should take 3 arguments: mysql username, mysql
        password and database name (no argument validation needed)
    - You must use the module MySQLdb (import MySQLdb)
    - Results must be sorted in ascending order by states.id
"""


import sys
import MySQLdb

if __name__ == "__main__":
    host = "localhost"
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    try:
        db = MySQLdb.connect(host="localhost", user, passwd, db)
        result = db.cursor()
        result.execute("SELECT states.id, states.name FROM states
                       ORDER BY states.id ASC")
        myRow = result.fetchall()
        for row in myRow:
            print(row)
    except:
        print("Could not display data")

    db.close()
