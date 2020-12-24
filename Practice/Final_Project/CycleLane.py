import sqlite3
import xlrd

conn = sqlite3.connect('./DB/CycleLane.db')
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS cycleLane;")
# 기간, 자치구, 구간합계, 길이합계, 자전거전용도로 구간, 자전거전용도로 길이, 자전거보행자겸용도로 구간, 자전거보행자겸용도로 길이, 자전거전용차로 구간, 자전거전용차로 길이, 자전거우선도로 구간, 자전거우선도로 길이
cur.execute("CREATE TABLE IF NOT EXISTS cycleLane  (year str, \
                                                                                                    region str, \
                                                                                                    totalNum int, \
                                                                                                    totalRange int, \
                                                                                                    cycleOnlyNum int, \
                                                                                                    cycleOnlyRange int, \
                                                                                                    multiuseNum int, \
                                                                                                    multiuseRange int, \
                                                                                                    cycleRoadNum int,\
                                                                                                    cycleRoadRange int,\
                                                                                                    cyclePriorityNum int, \
                                                                                                    cyclePriorityRange int);"
            )

print("자전거도로현황 테이블 생성 완료")

wb = xlrd.open_workbook('C:\\Pythonsource\\Class\\CBNU_Advanced_Business_Programming\\Practice\\Final_Project\\Data\\자전거도로현황\\서울시자전거도로현황.csv')


# cur.execute("DELETE FROM cycleLane;")

i = 0
sh = wb.sheet_by_index(0)
while i < (sh.nrows-3):
    cur.execute("INSERT INTO cycleLane VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
            ((str(sh.cell(i+3,0))).split(":")[1],\
             str(sh.cell(i+3,2)).split("'")[1],\
             str(sh.cell(i+3,3)).split(":")[1],\
             str(sh.cell(i+3,4)).split(":")[1],\
             str(sh.cell(i+3,5)).split(":")[1],\
             str(sh.cell(i+3,6)).split(":")[1],\
             str(sh.cell(i+3,7)).split(":")[1],\
             str(sh.cell(i+3,8)).split(":")[1],\
             str(sh.cell(i+3,9)).split(":")[1],\
             str(sh.cell(i+3,10)).split(":")[1],\
             str(sh.cell(i+3,11)).split(":")[1],\
            str(sh.cell(i+3,12)).split(":")[1]
             ))
    i = i + 1
conn.commit()
print("자전거도로현황 데이터 입력 완료")