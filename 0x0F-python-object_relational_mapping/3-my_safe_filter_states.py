#!/usr/bin/python3
"""
Once again, write a script that takes in arguments and displays
all values in the states table of hbtn_0e_0_usa where name matches
the argument. But this time, write one that is safe from MySQL injections!

    - Your script should take 4 arguments: mysql username, mysql password,
        database name and state name searched (safe from MySQL injection)
    - You must use the module MySQLdb (import MySQLdb)
    - Results must be sorted in ascending order by states.id
"""

import sys
import MySQLdb

if __name__ == "__main__":

    host = 'localhost'
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    state = sys.argv[4].split(' ')
    state = state[0]
    sql = "SELECT * FROM states WHERE name LIKE BINARY '{}'\
            ORDER BY id ASC".format(state)

    dbConn = MySQLdb.connect(host, user, passwd, db)
    result = dbConn.cursor()

    try:
        result.execute(sql)
        myRows = result.fetchall()
        for row in myRows:
            print(row)
    except:
        print("Could not display data")

    dbConn.close()
