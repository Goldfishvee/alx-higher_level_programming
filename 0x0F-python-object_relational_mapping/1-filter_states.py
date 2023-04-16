#!/usr/bin/python3
"""This script will search for entries beginning with a specified letter"""

import MySQLdb
import sys

if __name__ == '__main__':
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # connect to database
    try:
        db = MySQLdb.connect(host="localhost",
                             user=mysql_username,
                             passwd=mysql_password,
                             db=database_name,
                             port=3306)
        cur = db.cursor()
    except MySQLdb.Error as e:
        print(f"MySQLdb Error {e.args[0]}: {e.args[1]}")
        sys.exit(1)

    # execute search query
    try:
        cur.execute("""SELECT * FROM states WHERE name LIKE BINARY 'N%'
                    ORDER BY states.id""")
        states = cur.fetchall()
    except MySQLdb.Error as e:
        print(f"MySQLdb Error {e.args[0]}: {e.args[1]}")

    # print results
    for state in states:
        print(state)

    # clean up
    cur.close()
    db.close()
