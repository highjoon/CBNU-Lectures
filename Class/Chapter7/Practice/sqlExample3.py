import sqlite3

conn = sqlite3.connect("test.db")
cur = conn.cursor()

# sql = "SELECT * FROM Customer WHERE LastName = ? AND Company = ?"
# cur.execute(sql, ('Cho', 'Samsung'))

sql = "SELECT * FROM Customer WHERE LastName = :name"
cur.execute(sql, {"name" : 'Cho'})

rows = cur.fetchall()
for row in rows:
    print(row)
conn.close()