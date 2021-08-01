import sqlite3 as lite
import sys
try:
    con = lite.connect('test4.db')
    cur = con.cursor()
    cur.executescript("""
        DROP TABLE IF EXISTS Cars;
        CREATE TABLE Cars (Id INT, Name TEXT, Price INT);
        INSERT INTO Cars VALUES (1, 'Audi', 52642);
        INSERT INTO Cars VALUES (2, 'Mercedes', 57127);
        INSERT INTO Cars VALUES (3, 'Skoda', 9000);
        INSERT INTO Cars VALUES (4, 'Volvo', 29000);
        INSERT INTO Cars VALUES (5, 'Bently', 350000);
        INSERT INTO Cars VALUES (6, 'Citroen', 21000);
        INSERT INTO Cars VALUES (7, 'Hummer', 41400);
        INSERT INTO Cars VALUES (8, 'Volkswagen', 21600);
    """)
    # DROP TABLE IF EXISTS : 존재하면 삭제해라.

    cur.execute('SELECT * FROM Cars;')
    rows = cur.fetchall()
    for row in rows:
        print(row)

    con.commit()

except lite.Error:
    if con:
        con.rollback()
    #     ROLLBACK 명령어는 Transaction 이 시작된 이후로 수행된 모든 연산을 취소하고, DB 를 Transaction 이 시작된 시점으로 복원한다.
    #     즉, 맨 처음에 선언했던 DB로 돌아간다.
    print("Error %s : " % lite.Error.args[0])
    sys.exit(1)

finally:
    if con:
        con.close()

"""
try 블록 수행 중 오류가 발생하면 except 블록이 수행된다. 

하지만 try 블록에서 오류가 발생하지 않는다면 except 블록은 수행되지 않는다.

try문에는 finally절을 사용할 수 있다. 

finally절은 try문 수행 도중 예외 발생 여부에 상관없이 항상 수행된다. 

보통 finally절은 사용한 리소스를 close해야 할 때에 많이 사용한다.
"""