# 제목과 축이름

import matplotlib.pyplot as plt

# 방법 2 : 각각 plt.title(), plt.xlabel(), plt.ylabel()에 기입함.
fig, ax = plt.subplots(1,1)
ax.plot([1,2,3], [1,2,3])
ax.set_title("Graph Title")
ax.set_xlabel("x-axis title")
ax.set_ylabel("y-axis title")
plt.show()