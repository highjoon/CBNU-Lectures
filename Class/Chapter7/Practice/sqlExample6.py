import sqlite3 as lite
import sys
try:
    conn = lite.connect('test.db')
    cur = conn.cursor()
    cur.executescript("""
          DROP TABLE IF EXISTS Cars;
          CREATE TABLE Cars(Id INT, Name TEXT, Price INT);
          INSERT INTO Cars VALUES(1,'Audi',52642);
          INSERT INTO Cars VALUES(2,'Mercedes',57127);
          INSERT INTO Cars VALUES(3,'Skoda',9000);
          INSERT INTO Cars VALUES(4,'Volvo',29000);
          INSERT INTO Cars VALUES(5,'Bentley',350000);
          INSERT INTO Cars VALUES(6,'Citroen',21000);
          INSERT INTO Cars VALUES(7,'Hummer',41400);
          INSERT INTO Cars VALUES(8,'Volkswagen',21600);
          """)

    cur.execute('SELECT * FROM Cars')
    rows = cur.fetchall()
    for row in rows:
        print(row)

    conn.commit()

except lite.Error:
    if conn:
        conn.rollback()
    print("ERROR %s: " % lite.Error.args[0])
    sys.exit()

finally:
    if conn:
        conn.close()