import sqlite3
import xlrd

conn = sqlite3.connect('./DB/RentalCenter.db')
cur = conn.cursor()
# cur.execute("DELETE FROM RentalCenter;")
cur.execute("DROP TABLE IF EXISTS rentalCenter;")

# 자치구
cur.execute("CREATE TABLE IF NOT EXISTS rentalCenter (region str, name str);")

print("대여소 정보 테이블 생성 완료")

wb = xlrd.open_workbook('C:\\Pythonsource\\Class\\CBNU_Advanced_Business_Programming\\Practice\\Final_Project\\Data\\대여소 및 대여소별 이용정보\\공공자전거 대여소 정보(20.07.13 기준).xlsx')
sh = wb.sheet_by_index(1)

i = 0
while i < (sh.nrows - 1):
    cur.execute("INSERT INTO rentalCenter VALUES (?,?)",
                (((str(sh.cell(i+1,2))).split(":")[1])[1:-1],\
                 (str(sh.cell(i+1,1)).split(":")[1])[1:-1],))
    i += 1

print("대여소 정보 데이터 입력 완료")

conn.commit()
conn.close()

