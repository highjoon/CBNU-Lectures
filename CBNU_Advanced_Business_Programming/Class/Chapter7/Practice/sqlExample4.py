import sqlite3

conn = sqlite3.connect("test2.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS customer(PersonID text, LastName text, FirstName text, Salary int, Company text);")


data = (
    ('1', 'Cho', 'Wan-Sup', 50000, 'Samsung'),
    ('2', 'Kim', 'Jung-su', 45000, 'Hyndai'),
    ('3', 'Park', 'Jeong-hee', 34500, 'Samsung')
)

sql = "INSERT INTO Customer (PersonID, LastName, FirstName, Salary, Company) VALUES (?, ?, ?, ?, ?)"
cur.executemany(sql, data)

cur.execute("SELECT * FROM Customer;")
for row in cur:
    print(row)

conn.commit()
conn.close()