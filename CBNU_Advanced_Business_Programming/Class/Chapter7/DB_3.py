import sqlite3
con = sqlite3.connect('test2.db')
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Company (Cname text, City text, Phone text);")
cur.execute("INSERT INTO Company VALUES ('Samsung', 'Seoul', '123-5678');")
cur.execute("INSERT INTO Company VALUES ('Hyundai', 'Busan', '453-7561');")
cur.execute("SELECT * FROM Company;")

for row in cur:
    print(row)

con.commit()
con.close()