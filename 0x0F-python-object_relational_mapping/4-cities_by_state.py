#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0e_4_usa"""
from MySQLdb import connect
from sys import argv

if __name__ == "__main__":
    db_connect = connect(user=argv[1], password=argv[2], db=argv[3],
                         host="localhost", port=3306)
    cur = db_connect.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                   FROM cities JOIN states WHERE states.id = cities.state_id
                   """)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db_connect.close()
