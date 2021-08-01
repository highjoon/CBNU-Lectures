"""
직각 삼각형 밑변과 높이 입력받아 빗변 길이 출력
입력은 실수로
"""
import math

b = float(input("밑변 : "))
h = float(input("높이 : "))
a = math.hypot(b,h)
print(a)