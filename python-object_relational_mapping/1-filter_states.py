#!/usr/bin/python3
"""List all states from a given db sorted in ascending order by id"""


import MySQLdb
import sys

if __name__ == "__main__":
    user_db = sys.argv[1]
    passwd_db = sys.argv[2]
    name_db = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost", user=user_db, passwd=passwd_db, db=name_db, port=3306
    )

    querie = db.cursor()

    querie.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC")

    results = querie.fetchall()

    for element in results:
        print(element)

    db.close()
