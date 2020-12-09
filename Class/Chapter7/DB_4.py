import sqlite3

con  = sqlite3.connect('test2.db')
cur = con.cursor()

cur.execute('SELECT * FROM Company;')
a = cur.fetchone()
b = cur.fetchmany(2)
c = cur.fetchall()

print(a)
print(b)
print(c)