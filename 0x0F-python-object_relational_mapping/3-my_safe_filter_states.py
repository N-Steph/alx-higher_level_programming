#!/usr/bin/python3
"""Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument. Making it safe from
MySQL injections
"""
from MySQLdb import connect
from sys import argv

if __name__ == "__main__":
    db_connect = connect(user=argv[1], password=argv[2], db=argv[3],
                         host="localhost", port=3306)
    cur = db_connect.cursor()
    argument = argv[4].split("'")[0]
    cur.execute("""SELECT id, name FROM states
                 WHERE name LIKE BINARY'{}' ORDER BY states.id"""
                .format(argument))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db_connect.close()
