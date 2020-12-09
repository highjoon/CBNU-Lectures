# Histogram

import matplotlib.pyplot as plt
import numpy as np

# numpy.random.seed(n)을 이용하여 임의의 시드를 생성할 수 있습니다. 시드 값에 따라 난수와 흡사하지만 항상 같은 결과를 반환합니다.
np.random.seed(0)

# random.randn : 가우시안 표준 정규 분포에서 난수 matrix array 생성.
x = np.random.randn(1000)
plt.title("Histogram")

# arrays : 데이터를 넣고자하는 x축.
# bins : 해당 막대의 영역을 얼마나 채우는지 표시. (생성되는 막대의 개수라고 볼 수 있음)

arrays, bins, patches = plt.hist(x, bins=10)
plt.show()