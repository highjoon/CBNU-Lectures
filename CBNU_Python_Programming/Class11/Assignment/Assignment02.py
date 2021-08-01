import sqlite3 as sq

conn = sq.connect("CbnuFC.db")
cur = conn.cursor()

playerTable = "CREATE TABLE IF NOT EXISTS Players (PlayerID id INTEGER PRIMARY KEY, Pname text," \
              "Position text, BackNum int, Height int); "

cur.execute(playerTable)

playerList = ()

id = int(input("선수 ID 입력 : "))
playerName = str(input("선수 이름 입력 : "))
position = str(input("포지션 입력 : "))
backNum = int(input("등번호 입력 : "))
height = int(input("키 입력 : "))

playerSQL = "INSERT INTO Players (PlayerID, Pname, TeamCode, Position, BackNum, Height) VALUES (?, ?, ?, ?, ?, ?)"

cur.executemany(playerSQL, playerList)
