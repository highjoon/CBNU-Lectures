import sqlite3
conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute('SELECT * FROM Customer;')
    rows = cur.fetchall()
    for row in rows:
        print(row)