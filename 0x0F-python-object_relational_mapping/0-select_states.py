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
    dbname = sys.argv[3]

    db = MySQLdb.connect(host, user, passwd, dbname)
    result = db.cursor()

    sql = "SELECT * FROM states ORDER BY states.id ASC;"

    try:
        result.execute(sql)
        myRows = result.fetchall()
        for row in myRows:
            print(row)
    except:
        print("Could not display data")

    db.close()
