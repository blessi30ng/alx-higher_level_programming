#!/usr/bin/python3

from sys import argv
import MySQldb

if __name__ == '__main__':
    conn = MySQldb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    sql = "SELECT FROM states WHERE name == %s"
    cur.execute(sql, (argv[4]))
    result = cur.fetchall()
    for r in result:
        print(r)
    cur.close()
    conn.close()
