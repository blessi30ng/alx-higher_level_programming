#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    sql = "SELECT FROM states WHERE name LIKE 'N%'"
    cur.execute(sql)
    myresult = cur.fetchall()
    for r in myresult:
        print(r)
    cur.close()
    conn.close()
