#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.

    - Your script should take 4 arguments: mysql username, mysql
        password, database name and state name searched (no argument
        validation needed)
    - You must use the module MySQLdb (import MySQLdb)
    - Your script should connect to a MySQL server running on localhost
        at port 3306
    - You must use format to create the SQL query with the user input
    - Results must be sorted in ascending order by states.id
    - Results must be displayed as they are in the example below
"""


import sys
import MySQLdb

if __name__ == "__main__":
    host = "localhost"
    user = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]
    state = sys.argv[4]
    sql = "SELECT states.id, states.name FROM states WHERE \
            states.name='state' ORDER BY states.id ASC;"

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
