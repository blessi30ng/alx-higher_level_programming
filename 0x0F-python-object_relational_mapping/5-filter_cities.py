#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3], charset="utf-8")
    cur = conn.cursor()
    sql = "SELECT c.name \
            FROM states s \
            INNER JOIN cities as c \
                ON c.state_id = s.id \
            WHERE s.name LIKE %s \
            ORDER BY c.id ASC" 
    cur.execute(sql, (argv[4], ))
    result = cur.fetchall()
    for r in result:
        print(r)
    cur.close()
    conn.close()
