#!/usr/bin/python3
# 1-select_states.py
# Ikundwila Mwambona <ikumwana@gmail.com>
"""
This script lists all states with a name starting with
Upper N in the database hbtn_0e_0_usa.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY `id`")
    states = cur.fetchall()
    for state in states:
        if state[1][0] == "N":
            print(state)
