import sqlite3

conn = sqlite3.connect("Practice.db")
cur = conn.cursor()

PnameSQL = "SELECT Pname, TeamName FROM Players, Teams WHERE Players.TeamCode = Teams.TeamCode;"
Pname = cur.execute(PnameSQL)

for r in Pname:
    print("%s / %s" % (r[0], r[1]))

conn.commit()
conn.close()