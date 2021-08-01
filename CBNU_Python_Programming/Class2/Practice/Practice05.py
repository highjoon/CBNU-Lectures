"""
실습 5) 나무의 높이 구하기

다음과 같이 관측자의 키(h),
관측자와 나무 사이의 거리(d),
관측자가 나무의 끝을 보았을 때의 각(a)를 알 때,
나무의 높이를 구하는 프로그램을 작성하여라.
(h, d, a는 입력 받는다, a는 degree 값)
"""
import math

h = float(input("키 : "))
d = float(input("나무 사이의 거리 : "))
a = float(input("나무의 끝을 보았을 때의 각 : "))

degree = math.radians(a)

result = h + (d * math.tan(degree))
# 키 + (나무 사이의 거리 x tan(degree))

print(result)