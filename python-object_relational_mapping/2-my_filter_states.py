#!/usr/bin/python3
"""Script that takes in an argument and displays
all values in the states table where name matches"""
import sys
import MySQLdb

if __name__ == "__main__":
    database = MySQLdb.connect(user=sys.argv[1],
                               passwd=sys.argv[2],
                               db=sys.argv[3])
    curs = database.cursor()
    curs.execute('SELECT * FROM `states` \
                 WHERE `name` = %s \
                 ORDER BY `id` ASC;', (sys.argv[4],))
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    database.close()
