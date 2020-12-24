import sqlite3
import xlrd

conn = sqlite3.connect('./DB/RentalUse.db')
cur = conn.cursor()
cur.execute("DELETE FROM rentalUse;")
cur.execute("DROP TABLE IF EXISTS rentalUse;")
# 대여소그룹 (자치구), 대여일자, 대여건수
cur.execute("CREATE TABLE IF NOT EXISTS rentalUse  (region str, \
                                                                                                    date str, \
                                                                                                    num str);"
            )
print("대여소별 이용정보 테이블 생성 완료")
wb201906_201911 = xlrd.open_workbook('C:\\Pythonsource\\Class\\CBNU_Advanced_Business_Programming\\Practice\\Final_Project\\Data\\대여소 및 대여소별 이용정보\\공공자전거 대여소별 이용정보_201906_201911.xlsx')
wb201912_202005 = xlrd.open_workbook('C:\\Pythonsource\\Class\\CBNU_Advanced_Business_Programming\\Practice\\Final_Project\\Data\\대여소 및 대여소별 이용정보\\공공자전거 대여소별 이용정보_201912_202005.xlsx')
wb202006 = xlrd.open_workbook('C:\\Pythonsource\\Class\\CBNU_Advanced_Business_Programming\\Practice\\Final_Project\\Data\\대여소 및 대여소별 이용정보\\공공자전거 대여소별 이용정보_202006.xlsx')

sh201906_201911 = wb201906_201911.sheet_by_index(0)
sh201912_202005 = wb201912_202005.sheet_by_index(0)
sh202006 = wb202006.sheet_by_index(0)

def toSQL(sh):
    i = 0
    while i < (sh.nrows - 1):
        cur.execute("INSERT INTO rentalUse VALUES (?,?,?)",
                     (((str(sh.cell(i + 1, 0))).split(":")[1])[1:-1], \
                     ((str(sh.cell(i + 1, 2))).split(":")[1]), \
                     ((str(sh.cell(i + 1, 3))).split(":")[1]), \
                     ))
        i += 1

toSQL(sh201906_201911)
toSQL(sh201912_202005)
toSQL(sh202006)
print("대여소별 이용정보 데이터 입력 완료")

conn.commit()