import sqlite3

conn = sqlite3.connect("Practice.db")
cur = conn.cursor()

while True :
    name = input("팀 이름을 입력하세요 : ")
    if name != "종료":
        SQL = "SELECT TeamCode FROM Teams WHERE TeamName = :Name"
        code = cur.execute(SQL, {"Name": name})

        for row in code:
            SQL2 = "SELECT Pname, Position FROM Players WHERE TeamCode = :Code"
            players = cur.execute(SQL2, {"Code": row[0]})
            for r in players:
                print("%s / %s" % (r[0], r[1]))
    else:
        print("종료되었습니다.")
        break

conn.commit()
conn.close()