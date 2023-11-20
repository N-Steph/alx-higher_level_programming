#!/usr/bin/python3
"""This script selects all rows in states table from a database"""
from MySQLdb import connect
import sys

if __name__ == "__main__":
    db_connect = connect(user=sys.argv[1], password=sys.argv[2],
                         db=sys.argv[3], host="localhost", port=3306)
    cur = db_connect.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print("{}".format(row))
    cur.close()
    db_connect.close()
