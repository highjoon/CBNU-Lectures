"""
양의 정수 N을 입력 받아 N의 약수를 출력하는 프로그램을 작성하시오.

Hint.

1 ~ N까지의 수를 하나씩 순회하면서 순회하는 수 i가 N을 나누어 나머지가 0일 때,
i는 N의 약수이다.

즉, N % i == 0일 때, i는 N의 약수

"""
import sys

N = int(input("양의 정수 : "))
i = 1

if N <= 0:
    print("에러")
    sys.exit()

"""
while i <= N:
    if N % i == 0:
        print(i)
    i+=1
"""

for i in range(1, N+1):
    if N % i ==0:
        print(i)