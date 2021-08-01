# 제목과 축이름

import matplotlib.pyplot as plt

# 방법 1 : 각각 plt.title(), plt.xlabel(), plt.ylabel()에 기입.
plt.figure()
plt.plot([1,2,3], [1,2,3])
plt.title("Graph Title")
plt.xlabel("x-axis title")
plt.ylabel("y-axis title")
plt.show()