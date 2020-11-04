import sqlite3
import xlrd
import math
con = sqlite3.connect("testDB")
cur = con.cursor()
wb = xlrd.open_workbook('C:\\Pythonsource\\Class\\CBNU_Advanced_Technology_Programming\\Practice\\Practice2\\xlxs\\jejuVisitor.xlsx')
print("The number of worksheets is", wb.nsheets)
print("Worksheet name(s):", wb.sheet_names())
cur.execute("delete from jejutourist")
i=0
while i < wb.nsheets:
 sh = wb.sheet_by_index(i)
 print(sh.name, sh.nrows, sh.ncols)
 cur.execute("insert into jejutourist values (?,?,?,?,?,\
 ?,?,?,?,?,\
?,?,?,?,?,\
?,?,?,?,?)",
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
print("------ select * from jejutourist; ---------------------")
for row in cur.execute("select * from jejutourist;"):
 print(row)
