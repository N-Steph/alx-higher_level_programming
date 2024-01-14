#!/usr/bin/python3

"""
This scripts selects records from hbtn_0e_4_usa database.
In such a way that the resulting record consist of city id, city name and
state name from cities table and states table respectively
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    cur = db.cursor()
    query = """SELECT cities.id, cities.name, states.name \
               FROM cities, states \
               WHERE cities.state_id = states.id"""
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
