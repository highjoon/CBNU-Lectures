import sqlite3

conn = sqlite3.connect("Practice.db")
cur = conn.cursor()

PnameSQL = "SELECT Pname, Height FROM Players WHERE Height >= 177 ORDER BY Height ASC;"
Pname = cur.execute(PnameSQL)

for r in Pname:
    print("%s / %d" % (r[0], r[1]))

conn.commit()
conn.close()