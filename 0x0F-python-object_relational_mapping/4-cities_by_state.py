#!/usr/bin/python3
"""
Write a script that lists all cities from the database hbtn_0e_4_usa

    - Your script should take 3 arguments: mysql username, mysql
        password and database name
    - You must use the module MySQLdb (import MySQLdb)
    - Results must be sorted in ascending order by cities.id
"""


import sys
import MySQLdb

if __name__ == "__main__":

    host = "localhost"
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    dbConn = MySQLdb.connect(host, user, passwd, db)

    with dbConn.cursor() as result:
        result.execute("""
            SELECT
                cities.id, cities.name, states.name
            FROM
                states, cities
            WHERE
                cities.state_id = states.id
            ORDER BY
                cities.id
            ASC
            """)

        myRow = result.fetchall()

        for row in myRow:
            print(row)

        dbConn.close()
