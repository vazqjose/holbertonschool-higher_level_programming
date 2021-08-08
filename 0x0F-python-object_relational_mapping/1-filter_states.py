#!/usr/bin/python3
"""
Write a script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa:

    - Your script should take 3 arguments: mysql username,
        mysql password and
        database name (no argument validation needed)
    - You must use the module MySQLdb (import MySQLdb)
    - Your script should connect to a MySQL server running
        on localhost at port 3306
    - Results must be sorted in ascending order by states.id
    - Results must be displayed as they are in the example below
    - Your code should not be executed when imported
"""


import sys
import MySQLdb

if __name__ == "__main__":
    host = "localhost"
    user = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]
    sql = "SELECT states.id, states.name FROM states \
            WHERE states.name LIKE 'N%' OR LIKE 'n%' ORDER BY states.id ASC; "

    db = MySQLdb.connect(host, user, passwd, dbname)
    result = db.cursor()

    try:
        result.execute(sql)
        myRows = result.fetchall()
        for row in myRows:
            print(row)
    except:
        print("Could not display data")

    db.close()
