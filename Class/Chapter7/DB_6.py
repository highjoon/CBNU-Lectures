import sqlite3
con = sqlite3.connect('test3.db')
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Customer (PersonID text, LastName text, Firstname text, Salary int, Company text);")
# cur.execute("DELETE FROM Customer;")
data = (
    ('1', 'Cho', 'Wan-Sup', 50000, 'Samsung'),
    ('2', 'Kim', 'Jung-su', 45000, 'Hyundai'),
    ('3', 'Park', 'Jeong-hee', 34500, 'Samsung')
)
sql = "INSERT INTO Customer (PersonID, LastName, FirstName, Salary, Company) VALUES (?, ?, ?, ?, ?);"
cur.executemany(sql, data)

cur.execute("SELECT * FROM Customer;")
print("======================")
for row in cur:
    print(row)

con.commit()
con.close()