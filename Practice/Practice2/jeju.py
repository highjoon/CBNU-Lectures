import sqlite3
con = sqlite3.connect("testDB")
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS jejutourist;")
cur.execute("create table jejutourist(\
 year str,\
 month str,\
 d_individual int, \
 d_package int,\
 d_leisure int,\
 d_conference int,\
 d_rest int,\
 d_family int,\
 d_education int,\
 d_etc int,\
 f_japan int,\
 f_china int,\
 f_hongkong int,\
 f_taiwan int,\
 f_singapore int,\
 f_malasia int,\
 f_indonesia int,\
 f_vietnam int,\
 f_thailand int,\
 f_usa int)"
)
print("DB table created !")
con.commit()