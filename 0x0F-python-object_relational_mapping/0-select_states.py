#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT FROM states ORDER BY id ASC")
    myresult = cur.fetchall()
    for row in myresult:
        print(row)
    cur.close()
    conn.close()
