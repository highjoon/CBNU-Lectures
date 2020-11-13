# 범례표시 : plt.plot의 인자로 label을 설정해주고 plt.legend()에 기록함

import matplotlib.pyplot as plt

plt.figure()
plt.plot([1,2,3], [1,2,3], label="Group 0")
plt.legend()
plt.show()