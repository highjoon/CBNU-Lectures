# 여러개 그래프에서 적용

import matplotlib.pyplot as plt

plt, ax = plt.subplots(1, 2, figsize=(20, 5))

# 0번 그래프
ax[0].plot([1,2,3], [1,2,3])
ax[0].set_xticks([1,2,3])

# 1번 그래프
ax[1].plot([1,2,3], [1,2,3])
ax[1].set_xlim([0,5])
plt.show()