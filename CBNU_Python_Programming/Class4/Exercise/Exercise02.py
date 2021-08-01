"""
예제 2) 위 예제 1은 음수를 입력하면 문제가 발생한다. 음수를 입력하면 '잘못된 입력'이라고 출력하고 프로그램을 종료하도록 업그레이드하여라.
"""
import sys
n = int(input('양의 정수 입력: '))
i = 1

if n <= 0:
    print('잘못된 입력')
    sys.exit()

while i <= n:
    print(i)
    i += 1