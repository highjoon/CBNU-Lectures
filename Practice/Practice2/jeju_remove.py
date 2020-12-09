import sqlite3
con = sqlite3.connect('testDB.db')
cur = con.cursor()
cur.execute("DROP TABLE jejutourist")
print("DB 테이블 제거 완료 !")
con.commit()