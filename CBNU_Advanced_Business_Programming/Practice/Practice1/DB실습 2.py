import sqlite3

conn = sqlite3.connect("Practice.db")
cur = conn.cursor()

PlayerList = (
    (4, '차범근', 'K03', 'FW', 11, 177),
    (5, '손흥민', 'K02', 'FW', 1, 178),
    (6, '김병지', 'K07', 'GK', 15, 182),
    (7, '염기훈', 'K07', 'MF', 75, 188),
    (8, '설기현', 'K07', 'MF', 87, 173),
    (9, '조원희', 'K03', 'MF', 12, 195),
    (10, '이동국', 'K03', 'FW', 46, 171),
    (11, '안정환', 'K02', 'FW', 64, 162),
    (12, '이천수', 'K02', 'MF', 23, 168),
    (13, '이승우', 'K03', 'MF', 71, 172),
    (14, '이강인', 'K03', 'MF', 19, 173),
    (15, '지동원', 'K02', 'FW', 20, 180)
)

PlayerSQL = "INSERT INTO Players (PlayerID, Pname, TeamCode, Position, BackNum, Height) VALUES (?, ?, ?, ?, ?, ?)"
cur.executemany(PlayerSQL, PlayerList)

conn.commit()
conn.close()