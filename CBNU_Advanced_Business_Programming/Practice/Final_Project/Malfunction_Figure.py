import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

plt.rcParams['font.family'] = 'NanumGothic'
conn = sqlite3.connect('./DB/Malfunction.db')
cur = conn.cursor()

a = cur.execute("SELECT type, count(*) AS mal_num FROM malfunction GROUP BY type ORDER BY mal_num DESC;")
avgList = []
for i in a:
    avgList.append(i[1])

labels = ['기타', '단말기', '안장', '잠금잠치 불량', '체인', '타이어', '파손', '페달']
sizes = avgList
colors = ['red', 'green', 'yellow', 'lightcoral', 'lightskyblue', 'yellowgreen', 'black', 'purple']
plt.figure(figsize=(10, 7))
explode = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
plt.title("2015 ~ 2020 서울시 공공자전거 고장신고 내역", pad=30)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.legend(labels)
plt.show()
