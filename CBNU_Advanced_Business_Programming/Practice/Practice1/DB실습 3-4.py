import sqlite3

conn = sqlite3.connect("Practice.db")
cur = conn.cursor()

while True :
    name = input("선수 이름을 입력하세요 : ")
    if name != "종료":
        SQL = "SELECT TeamCode FROM Players WHERE Pname = :Name"
        code = cur.execute(SQL, {"Name": name})

        for row in code:
            SQL2 = "SELECT TeamName, City FROM Teams WHERE TeamCode = :Code"
            teams = cur.execute(SQL2, {"Code": row[0]})
            for r in teams:
                print("%s / %s" % (r[0], r[1]))
    else:
        print("종료되었습니다.")
        break
        
conn.commit()
conn.close()