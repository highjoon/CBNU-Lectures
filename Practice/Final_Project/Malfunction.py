import sqlite3
import xlrd

conn = sqlite3.connect('./DB/Malfunction.db')
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS malfunction;")

# cur.execute("DELETE FROM malfunction;")

# 고장구분
cur.execute("CREATE TABLE IF NOT EXISTS malfunction  (type str);")

print("고장신고내역 테이블 생성 완료")

wb = xlrd.open_workbook('C:\\Pythonsource\\Class\\CBNU_Advanced_Business_Programming\\Practice\\Final_Project\\Data\\고장신고내역\\서울시 공공자전거 고장신고 내역_2015_2020.10.xlsx')
sh = wb.sheet_by_index(0)

i = 0
while i < (sh.nrows - 1):
    cur.execute("INSERT INTO malfunction VALUES (?)",
                ((str(sh.cell(i+1,2))).split("'")[1],))
    i += 1
    
print("고장신고내역 데이터 입력 완료")

conn.commit()
conn.close()
