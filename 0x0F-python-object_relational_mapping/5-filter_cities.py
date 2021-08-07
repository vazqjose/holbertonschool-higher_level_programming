#!/usr/bin/python3
"""
Write a script that lists all cities from the database hbtn_0e_4_usa

    - Your script should take 4 arguments: mysql username, mysql
        password, database name and state name (SQL injection free!)
    - You must use the module MySQLdb (import MySQLdb)
    - Your script should connect to a MySQL server running on
        localhost at port 3306
    - Results must be sorted in ascending order by cities.id
    - You can use only execute() once
"""


import sys
import MySQLdb

dbConn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

with dbConn.cursor() as result:
    result.execute("""
        SELECT
            cities.name
        FROM
            states, cities
        WHERE
            cities.state_id = states.id
        AND
            states.name = %(state)s
        ORDER BY
            cities.id
        ASC
        """, {
            'state': sys.argv[4]
        })

    myRow = result.fetchall()

    for row in myRow:
        print(row)

    dbConn.close()
