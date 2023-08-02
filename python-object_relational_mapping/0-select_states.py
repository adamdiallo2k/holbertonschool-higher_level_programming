#!/usr/bin/env python3
""" Script that lists all states from the database hbtn_0e_0_usa. """

import MySQLdb
import sys

if __name__ == "__main__":
    """ Get command line arguments """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """ Connect to the MySQL server"""
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database, port=3306)

    """Create a cursor"""
    cursor = db.cursor()

    """Execute SQL query"""
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    """Fetch all the rows"""
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    """Close the connection"""
    cursor.close()
    db.close()
