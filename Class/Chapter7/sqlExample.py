import sqlite3

con = sqlite3.connect("test.db")
cur = con.cursor()

cur.execute("CREATE TABLE Company (id INTEGER PRIMARY KEY, Cname text, City text, Phone text);")
cur.execute("CREATE TABLE Customer (id VARCHAR PRIMARY KEY, LastName text, FirstName text, Salary text, Company text);")

companyList = (
    (1, 'Samsung', 'Seoul', '123-5678'),
    (2, 'Hyundai', 'Busan', '345-4567'),
    (3, 'Hynix', 'ChengJu', '456-6789')
)

customerList = (
    ('P1', 'Cho', 'Wan-Sup', '50K', 'Samsung'),
    ('P2', 'Yoon', 'SangJoon', '35K', 'Hyundai'),
    ('P3', 'Hong', 'GilDong', '60K', 'Hynix')
)

cur.executemany("INSERT INTO Company (id, Cname, City, Phone) VALUES (?, ?, ?, ?)", companyList)
cur.executemany("INSERT INTO Customer (id, LastName, FirstName, Salary, Company) VALUES (?, ?, ?, ?, ?)", customerList)

for row in cur:
    print(row)

con.commit()
con.close()