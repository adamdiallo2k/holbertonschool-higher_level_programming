#!/usr/bin/python3
"""
List all cities of a state from the database
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    state_name = sys.argv[4]
    cur.execute("""SELECT cities.name  FROM cities
                INNER JOIN states ON cities.state_id = states.id
                WHERE states.name = %s ORDER BY cities.id ASC""", (state_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
