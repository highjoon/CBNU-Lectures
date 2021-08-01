"""
숫자 맞추기 게임) 1 ~ 100 사이의 임의의 수를 생성하고,
사용자가 생성된 숫자를 맞추는 프로그램을 작성하라.

게임 규칙)

예를 들어 무작위로 생성된 수가 77이라고 가정했을 때,
플레이어가 처음에 40을 입력하면 77은 40보다 크므로,
'더 큰 수입니다.'라고 출력,

다시 90을 입력하면, '더 작은 수입니다.'라고 출력하면서
플레이어가 맞춰야 할 숫자의 범위를 좁혀 가서
맞출 수 있도록 한다.

최종적으로 77을 입력하면 '
맞췄습니다'라고 출력하고
프로그램을 종료.
"""
import random

num = random.randint(1, 100)

while True:
    i = int(input("숫자 : "))

    if i < num:
        print("더 큰수")
    elif i > num:
        print("더 작은수")
    else:
        break
    print("정답!")