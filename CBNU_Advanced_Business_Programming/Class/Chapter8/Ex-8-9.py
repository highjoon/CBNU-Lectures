# x축, y축 단위와 범위 바꾸기

import matplotlib.pyplot as plt

# 1. 축 단위 바꾸기
# plt.xticks([단위 리스트]) 를 사용하면 x축 단위를 수동으로 바꿀 수 있다.
# y축도 마찬가지다.
# xticks()를 실행하지 않으면 디폴트 눈금 제공.

plt.figure()
plt.plot([1,2,3], [1,2,3])
# plt.xticks([1,2,3]) # x축 단위 바꾸기
# plt.yticks([1,2,3]) # y축 단위 바꾸기
plt.show()