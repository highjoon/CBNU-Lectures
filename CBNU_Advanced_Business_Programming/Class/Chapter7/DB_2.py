import sqlite3

con = sqlite3.connect('test.db')
cur = con.cursor()

cur.execute('SELECT * FROM Customer;')
for i in cur:
    print(i)

cur.execute('SELECT LastName, Salary FROM Customer;')
for i in cur:
    print(i)

cur.execute('SELECT * FROM Customer WHERE Salary > "46K";')
for i in cur:
    print(i)

cur.execute('SELECT * FROM Customer C, Company P WHERE C.Company = P.Cname')
for i in cur:
    print(i)

cur.execute('SELECT * FROM Customer C, Company P WHERE C.Company = P.Cname')
for i in cur:
    print(i)