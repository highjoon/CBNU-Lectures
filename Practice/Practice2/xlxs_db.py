import sqlite3
import xlrd
import math
con = sqlite3.connect("testDB.db")
cur = con.cursor()
wb = xlrd.open_workbook('C:\\Pythonsource\\Class\\CBNU_Advanced_Business_Programming\\Practice\\Practice2\\xlxs\\jejuVisitor.xlsx')

# 엑셀 시트 갯수
print("The number of worksheets is", wb.nsheets)

# 각 엑셀 시트의 이름
print("Worksheet name(s):", wb.sheet_names())

cur.execute("DELETE FROM jejutourist;")

i=0
while i < wb.nsheets:

 # 시트번호(인덱스)로 시트 가져오기
 sh = wb.sheet_by_index(i)

 # 시트이름, 행의 개수, 열의 개수
 # print(sh.name, sh.nrows, sh.ncols)

 # split :  아무 값도 넣어 주지 않으면 공백(스페이스, 탭, 엔터 등)을 기준으로 문자열을 나누어 준다.
 # a = "Life is too short"
 # a.split()
 # ['Life', 'is', 'too', 'short']

 # cell(행, 열)
 # 행, 열은 0 부터 시작.

 cur.execute("INSERT INTO jejutourist VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
 ((((str(sh.cell(2,6))).split("'"))[1])[:4],\
  (((str(sh.cell(0,0))).split())[1]).rstrip("월"),\
 ((str(sh.cell(7,6))).split(":"))[1],\
 ((str(sh.cell(11,6))).split(":"))[1],\
 ((str(sh.cell(22,6))).split(":"))[1],\
 ((str(sh.cell(24,6))).split(":"))[1],\
 ((str(sh.cell(26,6))).split(":"))[1],\
 ((str(sh.cell(28,6))).split(":"))[1],\
 ((str(sh.cell(30,6))).split(":"))[1],\
 ((str(sh.cell(32,6))).split(":"))[1],\
 ((str(sh.cell(36,6))).split(":"))[1],\
 ((str(sh.cell(38,6))).split(":"))[1],\
 ((str(sh.cell(40,6))).split(":"))[1],\
 ((str(sh.cell(42,6))).split(":"))[1],\
 ((str(sh.cell(44,6))).split(":"))[1],\
 ((str(sh.cell(46,6))).split(":"))[1],\
 ((str(sh.cell(48,6))).split(":"))[1],\
 ((str(sh.cell(50,6))).split(":"))[1],\
 ((str(sh.cell(52,6))).split(":"))[1],\
 ((str(sh.cell(56,6))).split(":"))[1],\
 ))

 i = i+1
con.commit()

print("------ SELECT * FROM jejutourist; ---------------------")
for row in cur.execute("SELECT * FROM jejutourist;"):
 print(row)


dh = wb.sheet_by_index(0)
"""
# [1] : 없으면 'text', '2016년' 이렇게 출력됨. 이 중에서 2번째 인덱스를 가져온다는 뜻. 즉 2016년.
# [:4] = 슬라이싱. 처음부터 인덱스3까지 가져옴. 즉 2016년 중 2016만 가져옴.
print((((str(dh.cell(2,6))).split("'"))[1])[:4] )
"""

"""
# [1]: 없으면 'number', '778483.0' 이렇게 출력되고 이 중에서 2번째 인덱스를 가져온다는 뜻. 즉 778483.0만 챙김
print((((str(dh.cell(7,6))).split(":"))[1]))
"""