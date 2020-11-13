# 1행 3열로 서브 그래프들을 그린다.

import matplotlib.pyplot as plt

# fig : 전체 그래프 (1개)
# ax : 서브 그래프 (3개)

fig, ax = plt.subplots(1,3)

# 각 서브 그래프들에 그래프를 그린다.
ax[0].plot([1,2,3], [1,2,3])
ax[1].bar([1,2,3], [1,2,3])
ax[2].pie([1,2,3])
plt.show()