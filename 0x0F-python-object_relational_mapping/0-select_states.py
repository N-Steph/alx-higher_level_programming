#!/usr/bin/python3

"""
This script uses MySQLdb module to connect to the hbtn_0e_usa database.
And SELECT all the state name together with their id in the states table
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    cur = db.cursor()
    cur.execute('SELECT * FROM states')  # Executes the SQL query
    row = cur.fetchall()  # Returns a list of tuple
    for row in row:
        print(row)
    cur.close()
    db.close()
