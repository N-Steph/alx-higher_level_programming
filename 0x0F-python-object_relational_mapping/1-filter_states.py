#!/usr/bin/python3

"""
This script uses the MySQL module to connect to the hbtn_0e_usa database
in mysql server.
And filter then print state name starting with N and id from the state table
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    cur = db.cursor()
    # execute sql query
    cur.execute('SELECT * FROM states WHERE name LIKE \'N%\'')
    row = cur.fetchall()  # Returns a list of tuple
    for row in row:
        print(row)
    cur.close()
    db.close()
