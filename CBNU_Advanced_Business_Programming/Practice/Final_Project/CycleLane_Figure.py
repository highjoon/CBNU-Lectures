import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

plt.rcParams['font.family'] = 'NanumGothic'
conn = sqlite3.connect('./DB/CycleLane.db')
cur = conn.cursor()

cur.execute("SELECT region, totalNum AS SumCycleLane \
                        FROM CycleLane \
                        GROUP BY region \
                        ORDER BY totalNum; ")

rows = cur.fetchall()
nda = np.asarray(rows)
y = nda[:,1]
x = np.arange(len(y))

xlabel = ['강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구', '동대문구', '동작구',
 '마포구', '서대문구', '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구',
 '중랑구']

colors = sns.color_palette('hls',len(xlabel))

plt.figure(figsize=(10, 7))
plt.title("2019년 서울시 자전거도로 현황")
plt.bar(x,y, width=0.7, align='center',color=colors, edgecolor=colors, alpha=0.7, linewidth=3)
plt.xticks(x, labels=xlabel, rotation=45, fontsize=9)
plt.yticks(y)
plt.xlabel("자치구")
plt.ylabel("구간 갯수")

plt.show()