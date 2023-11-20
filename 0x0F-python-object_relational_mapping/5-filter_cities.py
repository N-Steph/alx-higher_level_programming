#!/usr/bin/python3
"""Script that takes in the name of a state as an argument and lists all
cities of that state, using the databas hbtn_0e_4_usa
"""
from MySQLdb import connect
from sys import argv

if __name__ == "__main__":
    db_connect = connect(user=argv[1], password=argv[2], db=argv[3],
                         host="localhost", port=3306)
    cur = db_connect.cursor()
    cur.execute("""SELECT DISTINCT cities.name FROM cities JOIN states
                   WHERE cities.state_id = (
                   SELECT states.id FROM states WHERE states.name = "{}")
                   """.format(argv[4]))
    rows = cur.fetchall()
    counter = 0
    for row in rows:
        counter += 1
        for col in row:
            print(col, end="")
        if counter != len(rows):
            print(", ", end="")
        else:
            print()
    cur.close()
    db_connect.close()
