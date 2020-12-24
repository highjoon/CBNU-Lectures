import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

plt.rcParams['font.family'] = 'NanumGothic'
conn = sqlite3.connect('./DB/RentalCenter.db')
cur = conn.cursor()

cur.execute("SELECT region, COUNT(name) AS numName \
                        FROM rentalCenter \
                        GROUP BY region \
                        ORDER BY COUNT(name);")

rows = cur.fetchall()
nda = np.asarray(rows)
y = nda[:,1]
x = np.arange(len(nda))

xlabel = nda[:,0]

colors = sns.color_palette('hls',len(xlabel))

plt.figure(figsize=(10, 7))
plt.title("2020년 자치구별 공공자전거 대여소 갯수")
plt.bar(x, y, width=0.7, align='center',color=colors, edgecolor=colors, alpha=0.7, linewidth=3)
plt.xticks(x, labels=xlabel, rotation=45, fontsize=9)
plt.yticks(sorted(y))
plt.xlabel("자치구")
plt.ylabel("갯수")
plt.show()