# 점을 찍고 싶은 경우 marker를 표시함.
# 점의 모양은 다양하게 지정 가능함. (o, x 등)

import matplotlib.pyplot as plt

plt.figure()

# marker 인자를 같이 적는다.
plt.plot([1,2,3], [1,2,3], marker='o')

plt.show()