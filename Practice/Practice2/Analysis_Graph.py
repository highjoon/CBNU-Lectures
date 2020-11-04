import sqlite3
import matplotlib.pyplot as plt
import numpy as np
con = sqlite3.connect("testDB")
cur = con.cursor()

print("<===> 년 ==== 월 ====레저====회의====휴식====친지방문====교육")

cur.execute("SELECT month, SUM(d_leisure), SUM(d_conference), SUM(d_rest), SUM(d_family), SUM(d_education) AS dum_of_d_group \
FROM jejutourist GROUP BY month ORDER BY month;")

rows = cur.fetchall()
print(rows)

nda = np.asarray(rows)

x1 = nda[:,0]
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

plt.plot(x1, y1, '-ro', label="Leisure")
plt.plot(x1, y2, '-.mo', label="Conference")
plt.plot(x1, y3, ':go', label="Rest")
plt.plot(x1, y4, '-yo', label="Family")
plt.plot(x1, y5, '-.ks', label="Education")

plt.legend(loc='upper left')

plt.show()
