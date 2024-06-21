#!/usr/bin/python3
"""Script that lists all the cities of a state"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    database = MySQLdb.connect(user=argv[1],
                               passwd=argv[2],
                               db=argv[3])
    curs = database.cursor()
    curs.execute("SELECT cities.name FROM cities INNER JOIN states ON\
                  cities.state_id = states.id WHERE states.name = %s\
                  ORDER BY cities.id ASC", (argv[4],))
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    database.close()
