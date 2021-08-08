#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.

    - Results must be sorted in ascending order by states.id
"""


import sys
import MySQLdb

if __name__ == "__main__":
    host = "localhost"
    user = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]
    state = sys.argv[4]

    sql = "SELECT * FROM states WHERE name LIKE BINARY '{}'\
            ORDER BY id ASC;".format(state)

    dbConn = MySQLdb.connect(host, user, passwd, dbname)
    result = dbConn.cursor()

    try:
        result.execute(sql)
        myRow = result.fetchall()
        for row in myRow:
            print(row)
    except:
        print("Could not display data")

    dbConn.close()
