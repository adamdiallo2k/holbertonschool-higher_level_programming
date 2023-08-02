#!/usr/bin/python3
"""List all cities from the db by given state"""

import MySQLdb
import sys

if __name__ == "__main__":
    """Connexion to the database"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    """Defining the cursor"""
    cursor = db.cursor()

    """Execute the query"""
    cursor.execute(
        """
        SELECT cities.name
        FROM cities
        JOIN states
        ON states.id = cities.state_id
        WHERE states.name LIKE BINARY %s
        ORDER BY cities.id
        """, (sys.argv[4],)
    )

    """Get results of the query"""
    rows = cursor.fetchall()

    """Format the output into a string"""
    city_names = []
    for row in rows:
        city_names.append(row[0])
    string = ", ".join(city_names)
    print(string)

    """Close cursor session and connexion"""
    cursor.close()
    db.close()
