# 축 범위 바꾸기

import matplotlib.pyplot as plt

plt.figure()
plt.plot([1,2,3], [1,2,3])

# plt.xlim([보여줄 최소값, 보여줄 최대값]) 를 사용하면 된다. y축도 마찬가지이다.
# x축 범위 바꾸기
plt.xlim([0,5])

# y축 범위 바꾸기
plt.ylim([0, 10])
plt.show()