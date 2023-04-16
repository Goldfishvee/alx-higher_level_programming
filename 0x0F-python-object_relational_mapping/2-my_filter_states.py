#!/usr/bin/python3
"""
This script will search and retrieve records from db based on state
inputted by user
Usage: <executable file command> <hostname> <password> <dbname>
       <'user-input-state'>
"""

import sys
import MySQLdb

if __name__ == '__main__':
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    # connect to database
    try:
        db = MySQLdb.connect(host="localhost",
                             user=mysql_username,
                             passwd=mysql_password,
                             db=database_name,
                             port=3306)
        cur = db.cursor()
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL db {e}")
        sys.exit(1)

    # Execute query search
    try:
        cur.execute("""SELECT * FROM states WHERE name LIKE BINARY '{}'
                    ORDER BY id""".format(state_name_searched))
        rows = cur.fetchall()
    except MySQLdb.Error as e:
        print("Error executing query {e}")

    # print results
    for row in rows:
        print(row)

    # clean up
    cur.close()
    db.close()
