# 막대 그래프

import matplotlib.pyplot as plt
import numpy as np # 수치계산 라이브러리

y = [2,3,1]

x = np.arange(len(y))   # 배열 [0,1,2]

# numpy.arange([start, ] stop, [step, ] dtype=None)
# numpy 모듈의 arange 함수는 반열린구간 [start, stop) 에서 step 의 크기만큼 일정하게 떨어져 있는 숫자들을 array 형태로 반환해 주는 함수다.

xlabel = ['a', 'b', 'c']

plt.title("Bar Chart")
plt.bar(x,y)

# xticks(), yticks() 함수는 각각 X축, Y축에 눈금을 표시합니다.
# xticks(), yticks() 함수에 파이썬 리스트 또는 NumPy 어레이를 입력하면 눈금과 숫자 레이블이 표시됩니다.
plt.xticks(x, xlabel)
# plt.yticks(sorted(y))
plt.yticks(y)


plt.xlabel("abc")           # 가로 라벨 이름
plt.ylabel("count")       # 세로 라벨 이름
plt.show()