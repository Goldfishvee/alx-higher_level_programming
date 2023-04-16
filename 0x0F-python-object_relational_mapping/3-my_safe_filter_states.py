#!/usr/bin/python3
"""This script will perform the same function as '2-my_filter_states.py'
However, this will be made safe from MySQL injection
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
        print("Error connecting to MySQL database: {}".format(e))
        sys.exit(1)

    # execute query using paramterization (safe from SQL injection)
    try:
        query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id"
        cur.execute(query, (state_name_searched,))
        rows = cur.fetchall()
    except MySQLdb.Error as e:
        print("Error executing query: {}".format(e))
        sys.exit(1)

    # print results
    for row in rows:
        print(row)
    # clean up
    cur.close()
    db.close()
