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

if __name__ == "__main__":

    host = 'localhost'
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    state = sys.argv[4].split(' ')
    state = state[0]
    sql = "SELECT cities.id, cities.name, states.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            WHERE states.name LIKE BINARY '{}'\
            ORDER BY cities.id ASC".format(state)

    dbConn = MySQLdb.connect(host, user, passwd, db)
    result = dbConn.cursor()

    try:
        result.execute(sql)
        myRows = result.fetchall()
        cities = ''
        for row in myRows:
            cities += row[1]
            cities += ", "
        print(cities[:-2])

    except:
        print("Could not display data")
        dbConn.rollback

    dbConn.close()
