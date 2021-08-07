#!/usr/bin/python3
"""
Write a script that lists all states with a name starting with N (upper N) 
from the database hbtn_0e_0_usa:

    - Your script should take 3 arguments: mysql username, mysql password and
        database name (no argument validation needed)
    - You must use the module MySQLdb (import MySQLdb)
    - Your script should connect to a MySQL server running on localhost at port 3306
    - Results must be sorted in ascending order by states.id
    - Results must be displayed as they are in the example below
    - Your code should not be executed when imported
"""


import sys
import MySQLdb

db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

result = db.cursor()

result.execute(""" SELECT states.id, states.name FROM states WHERE states.name LIKE 'N%' ORDER BY states.id ASC """)

myRow = result.fetchall()

for row in myRow:
    print(row)
