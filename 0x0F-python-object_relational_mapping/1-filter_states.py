#!/usr/bin/python3
"""Scripts that lists all states with a name starting with N from the
database hbtn_0e_0_usa
"""
from MySQLdb import connect
from sys import argv

if __name__ == "__main__":
    db_connect = connect(user=argv[1], password=argv[2], db=argv[3],
                         host="localhost", port=3306)
    cur = db_connect.cursor()
    cur.execute("SELECT id, name FROM states WHERE name LIKE 'N%'")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db_connect.close()
