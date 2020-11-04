import sqlite3

conn = sqlite3.connect("Practice.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Players (PlayerID id INTEGER PRIMARY KEY, Pname text, TeamCode text, Position text, BackNum int, Height int);")
cur.execute("CREATE TABLE IF NOT EXISTS Teams (TeamCode id VARCHAR PRIMARY KEY, TeamName text, City text);")


PlayerList = (
    (1, '김남일', 'K03', 'DF', 33, 177),
    (2, '박지성', 'K07', 'MF', 7, 178),
    (3, '이영표', 'K02', 'MF', 22, 176)
)

TeamList = (
    ('K03', '스틸러스', '포항'),
    ('K07', '드래곤즈', '전남'),
    ('K02', '블루윙즈', '수원')
)

PlayerSQL = "INSERT INTO Players (PlayerID, Pname, TeamCode, Position, BackNum, Height) VALUES (?, ?, ?, ?, ?, ?)"
TeamSQL = "INSERT INTO Teams (TeamCode, TeamName, City) VALUES (?, ?, ?)"

cur.executemany(PlayerSQL, PlayerList)
cur.executemany(TeamSQL, TeamList)

conn.commit()
conn.close()