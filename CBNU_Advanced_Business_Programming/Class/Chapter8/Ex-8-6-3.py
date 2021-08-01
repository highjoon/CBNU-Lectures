# 여러개의 서브 그래프 설정

import matplotlib.pyplot as plt

# fig : 전체 그래프 (1개)
# ax : 서브 그래프 (3개)

fig, ax = plt.subplots(1,2,figsize=(20,5))

# 0번 그래프
ax[0].plot([1,2,3], [1,2,3], color='C0')
ax[0].set_title("First Graph title")
ax[0].set_xlabel("First Graph x-axis")
ax[0].set_ylabel("First Graph y-axis")

# 1번 그래프
ax[1].plot([1,2,3], [1,2,3], color='C1')
ax[1].set_title("Second Graph x-axis")
ax[1].set_ylabel("Second Graph y-axis")
plt.show()