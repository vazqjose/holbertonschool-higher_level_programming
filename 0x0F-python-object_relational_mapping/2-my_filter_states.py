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

dbConn = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

result = dbConn.cursor()

result.execute("SELECT states.id, states.name FROM states WHERE states.name = 'sys.argv[4]' ORDER BY states.id ASC")


