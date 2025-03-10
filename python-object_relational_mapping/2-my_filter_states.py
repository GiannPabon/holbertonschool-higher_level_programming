#!/usr/bin/python3
"""
Lists all states where name matches the argument from hbtn_0e_0_usa.
Usage: ./2-my_filter_states.py <mysql username> <mysql password> \
<database name> <state name>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )
    cursor = db.cursor()
    query = (
        "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC".format(
            sys.argv[4]
        )
    )
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
