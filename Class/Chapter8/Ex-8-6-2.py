# 각 액자들에 그래프를 그린다.

import matplotlib.pyplot as plt

# fig : 전체 그래프 (1개)
# ax : 서브 그래프 (3개)
# 1행 4열로 서브 그래프들을 그린다.
# figsize : 그래프의 크기나 세로-가로 비율 (가로 20인치, 세로 5인치)
fig, ax = plt.subplots(1,4, figsize=(20,5))

# matplotlib에 정의된 색상을 지정
ax[0].plot([1,2,3], [1,2,3], color='C0')

# 'red' 대신 'r'로 축약형
ax[1].plot([1,2,3], [1,2,5], color='r')

# 16진수 표기법으로 지정
ax[2].plot([1,2,3], [1,2,7], color='#aa1f3c')

# 0 ~ 1로 정규화된 rgb값 지정
ax[3].plot([1,2,3], [1,2,9], color=(0.5, 0.2, 0.1))

plt.show()