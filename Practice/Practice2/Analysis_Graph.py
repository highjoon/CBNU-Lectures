import sqlite3
import matplotlib.pyplot as plt
import numpy as np
con = sqlite3.connect("testDB.db")
cur = con.cursor()

print("<===> 년 ==== 월 ====레저====회의====휴식====친지방문====교육")

cur.execute("SELECT month, SUM(d_leisure), SUM(d_conference), SUM(d_rest), SUM(d_family), SUM(d_education) AS dum_of_d_group \
FROM jejutourist GROUP BY month ORDER BY month;")

# [(1, 374785, 231555, 2080917, 235801, 1534),
# (2, 335613, 203530, 1976549, 147641, 368),
# (3, 333324, 274725, 2103634, 157995, 60747),
# (4, 468871, 357645, 2410134, 85222, 170870.5),
# (5, 503166, 232107, 2412018, 101689, 199901),
# (6, 408261, 176667, 2663494, 117368, 38319),
# (7, 353988, 271441, 2709919, 103702, 6750),
# (8, 382254, 134951, 2923151, 39571, 11794),
# (9, 198955, 211211, 2548076, 250473, 60027),
# (10, 422551, 406042, 2168254, 224973, 178738),
# (11, 558080, 340653, 1996966, 145643, 33925),
# (12, 359838, 199950, 2227124, 128999, 5072)]
rows = cur.fetchall()
print(rows)

# numpy 배열화 (array()와 동작 차이는 없지만 array는 copy=true가 기본이고, asarray는 copy=false가 기본)
nda = np.asarray(rows)

# [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.]
x1 = nda[:,0]
print(x1)

# [374785. 335613. 333324. 468871. 503166. 408261. 353988. 382254. 198955. 422551. 558080. 359838.]
y1 = nda[:,1]

y2 = nda[:,2]

y3 = nda[:,3]

y4 = nda[:,4]

y5 = nda[:,5]

plt.figure()

plt.title('Monthly Total Visitor By Travel Purpose(2016-2018)')

plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])

plt.xlabel('Month')

plt.ylabel('Visitors')

# - 모양의 선, 빨강색, o 마커
plt.plot(x1, y1, '-ro', label="Leisure")

# -. 모양의 선, magenta색, o 마커
plt.plot(x1, y2, '-.mo', label="Conference")

# ... 모양의 선, 초록색, o 마커
plt.plot(x1, y3, ':go', label="Rest")

# - 모양의 선, 노랑색, o 마커
plt.plot(x1, y4, '-yo', label="Family")

# -. 모양의 선, 검은색, 네모 (square) 마커
plt.plot(x1, y5, '-.ks', label="Education")

plt.legend(loc='upper left')

plt.show()
