#!/usr/bin/python3
"""Lists all rows from the states table starting with N"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    cur.execute("""SELECT * FROM states WHERE name
                LIKE 'N%' ORDER BY states.id""")

    for row in cur.fetchall():
        print(row)

    db.close()
