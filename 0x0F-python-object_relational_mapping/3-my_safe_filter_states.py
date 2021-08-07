#!/usr/bin/python3
"""
Once again, write a script that takes in arguments and displays
all values in the states table of hbtn_0e_0_usa where name matches
the argument. But this time, write one that is safe from MySQL injections!

    - Your script should take 4 arguments: mysql username, mysql password,
        database name and state name searched (safe from MySQL injection)
    - You must use the module MySQLdb (import MySQLdb)
    - Your script should connect to a MySQL server running on localhost
        at port 3306
    - Results must be sorted in ascending order by states.id
    - Results must be displayed as they are in the example below
"""

import sys
import MySQLdb

dbConn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

with dbConn.cursor() as result:
    result.execute("""
        SELECT
            states.id, states.name
        FROM
            states
        WHERE
            states.name = %(name)s
        ORDER BY
            states.id
        ASC
        """, {
            'name': sys.argv[4]
        })

    myRow = result.fetchall()

    for row in myRow:
        print(row)

    dbConn.close()
