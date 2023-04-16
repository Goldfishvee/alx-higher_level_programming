#!/usr/bin/python3
"""This script will list all cities from the db 'hbtn_0e_4_usa'
using the name of state inputted by user (sql injection free)
Results will be sorted in ascending order by cities.id
Only one execute() function can used
"""

import sys
import MySQLdb

if __name__ == '__main__':
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # connect to database
    try:
        db = MySQLdb.connect(host="localhost",
                             user=mysql_username,
                             passwd=mysql_password,
                             db=db_name,
                             port=3306)
        cur = db.cursor()
    except MySQLdb.Error as e:
        print("Error connecting to MySQL db: {}".format(e))
        sys.exit(1)

    # execute query (make safe from sql injection)
    try:
        query = """SELECT cities.name FROM cities INNER JOIN states
                ON states.id=cities.state_id WHERE states.name=%s
                ORDER BY cities.id ASC"""
        cur.execute(query, (state_name,))
        rows = cur.fetchall()
    except MySQLdb.Error as e:
        print("Error executing MYSQL query: {}".format(e))
        sys.exit(1)
    # print results
    hdisp = list(row[0] for row in rows)
    print(*hdisp, sep=", ")
    # clean up
    cur.close()
    db.close()
