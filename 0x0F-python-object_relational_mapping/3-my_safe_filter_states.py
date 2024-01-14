#!/usr/bin/python3

"""
This script selects a record from the states table in hbtn_0e_0_usa database.
This is done using the MySQLdb module
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name = %s"
    # execute sql query
    cur.execute(query, (sys.argv[4),))
    row = cur.fetchall()  # Returns a list of tuple
    for row in row:
        print(row)
    cur.close()
    db.close()
