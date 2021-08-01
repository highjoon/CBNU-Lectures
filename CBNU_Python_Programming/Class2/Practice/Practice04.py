"""
실습 4) Heron's Formula

삼각형의 세변의 길이(a, b, c)를 알면, 헤론의 공식을 이용하여 삼각형의 넓이를 구할 수 있다.

𝑆= √(𝑠(𝑠 −𝑎)(𝑠−𝑏)(𝑠−𝑐))

여기서
𝑠=  (𝑎+𝑏+𝑐)/2

입출력 예

삼각형의 세변의 길이를 a, b, c를 입력하시오.
a: 10
b: 8
c: 7
삼각형의 넓이는 27.810744326608734 입니다.
"""
import math

print("삼각형의 세변의 길이를 a, b, c를 입력하시오.")
a = float(input("a : "))
b = float(input("b : "))
c = float(input("c : "))
s = (a + b + c) / 2
S = math.sqrt(s * (s - a) * (s - b) * (s - c))
print("삼각형의 넓이는 {0} 입니다.".format(S))