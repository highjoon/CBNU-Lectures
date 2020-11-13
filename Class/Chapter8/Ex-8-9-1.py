# 그래프의 단위를 [1,2,3]과 같이 숫자가 아니라 문자로 바꾸는 예제
# 한글 처리 문제

import matplotlib.pyplot as plt

plt.figure()
plt.plot([1,2,3], [1,2,3])

# x축 단위 바꾸기
plt.xticks([1,2,3], ['Mon', 'Tue', 'Wed'])
# y축 단위 바꾸기
plt.yticks([1,2,3], ['Low', 'Mod', 'High'])
plt.show()