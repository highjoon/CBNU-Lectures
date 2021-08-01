"""
실습 3) 직각삼각형의 빗변 구하기

입출력 예

밑변 입력: 10
높이 입력: 5
빗변의 길이는 11.180339887498949입니다.


"""

import math

b = float(input("밑변 입력 : "))
h = float(input("높이 입력 : "))
answer = math.hypot(b,h)

print("빗변의 길이는 {0}입니다.".format(answer))