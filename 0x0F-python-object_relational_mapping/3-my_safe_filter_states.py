#!/usr/bin/python3

from sys import argv
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3], charset="utf-8")
    cur = conn.cursor
    sql = "SELECT FROM states WHERE name LIKE %s ORDER BY id ASC"
    cur.execute(sql, (argv[4], ))
    result = cur.fetchall()
    for r in result:
        print(r)
    cur.close()
    conn.close()
