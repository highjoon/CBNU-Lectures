import sqlite3

con = sqlite3.connect("test.db")
cur = con.cursor()
cur.execute("CREATE TABLE  IF NOT EXISTS Company (Cname varchar(20), City varchar(20), Phone varchar(20));")
cur.execute("CREATE TABLE  IF NOT EXISTS Customer (PersonID varchar(20), LastName varchar(20), FirstName varchar(20), Salary varchar(20), Company varchar(20));")

companyList = (
    ("Samsumg", "Seoul", '123-3456'),
    ("Hyundai", "Busan", '345-4567')
)

customerList = (
    ("P1", "Cho", "Wan-Sup", "50K", "Samsung"),
    ("P2", "Kim", "Sung", "45K", "Hyundai")
)

cur.executemany("INSERT INTO Company (Cname, City, Phone) VALUES (?, ?, ?)", companyList)
cur.executemany('INSERT INTO Customer (PersonID, LastName, FirstName, Salary, Company) VALUES (?,?,?,?,?)', customerList)

con.commit()
con.close()