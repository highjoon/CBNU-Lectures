# 파이 그래프

import matplotlib.pyplot as plt

plt.figure()

# 각 파트 이름 리스트.
labels = ['Apple', 'Banana', 'Orange', 'Tomato']

# 각 파트가 차지하는 비율 리스트.
sizes = [15, 30, 45, 10]

# 각 파트의 색상 리스트.
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

explode = (0, 0.1, 0, 0)
plt.title("Pie Chart")

# autopct는 부채꼴 안에 표시될 숫자의 형식을 지정합니다. 소수점 몇자리까지 표시 설정.
# explode는 부채꼴이 파이 차트의 중심에서 벗어나는 정도를 설정합니다.
# shadow를 True로 설정하면, 파이 차트에 그림자가 표시됩니다.
# startangle는 부채꼴이 그려지는 시작 각도를 설정합니다. 디폴트는 0도 (양의 방향 x축)로 설정되어 있습니다. 90도는 12시 방향.
# counterclock=False로 설정하면 시계 방향 순서로 부채꼴 영역이 표시됩니다.
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.show()