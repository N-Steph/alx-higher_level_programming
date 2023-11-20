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
    argument = argv[4].split("'")[0]
    cur.execute("""SELECT DISTINCT cities.id, cities.name
                   FROM cities JOIN states
                   WHERE cities.state_id IN (
                   SELECT states.id FROM states WHERE states.name = "{}")
                   ORDER BY cities.id ASC""".format(argument))
    rows = cur.fetchall()
    counter = 0
    for row in rows:
        counter += 1
        print(row[1], end="")
        if counter != len(rows):
            print(", ", end="")
    print()
    cur.close()
    db_connect.close()
