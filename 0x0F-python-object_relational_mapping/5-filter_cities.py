#!/usr/bin/python3

"""
This script lists out all the cities found in a state from hbtn_0e_4_usa db
The state name is passed as a command line argument.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    cur = db.cursor()
    query = """SELECT cities.name \
               FROM cities \
               WHERE cities.state_id = (\
               SELECT states.id \
               FROM states \
               WHERE states.name = %(arg)s)"""
    cur.execute(query, {'arg': sys.argv[4]})
    rows = cur.fetchall()
    counter = 1
    for row in rows:
        if counter < len(rows):
            print(row[0] + ', ', end="")
        else:
            print(row[0])
        counter += 1
    cur.close()
    db.close()
