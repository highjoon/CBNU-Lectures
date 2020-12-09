# Stem Plot

import matplotlib.pyplot as plt
import numpy as np

# linspace(start, stop, num) / start : 배열의 시작값, stop : 배열의 끝값, num : start와 stop 사이를 몇 개의 일정한 간격으로 요소를 만들 것인지를 나타내는 값.
# np.pi : 원주율 (3.14)
x = np.linspace(0.1, 2 * np.pi, 10)
plt.title("Stem Plot")

# use_line_collection : 중간에 가로축 길게 그리기
# -.  :  선 모양
# np.cos(x) : x의 코사인 값
plt.stem(x, np.cos(x), '-.', use_line_collection=True)
plt.show()