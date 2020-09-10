print("윤상준")
print("hello world")
print("안녕하세요")

print()

# idle 에서는 print() 필요 없음

print(2+3)  # 5
print(2-3)  # -1
print(2*3)  # 6
print(2/3)  # 0.66666...
print(2//3) # 0
print(2%3)  # 2

print()

print("결과값은",2*7,"입니다.")
print("2 곱하기 7의 결과값은",2*7,"입니다.")

print()

# 온도 변환 프로그램    # ((화씨 - 32) x 5) / 9
# 화씨 온도 -> 섭씨 온도    화씨 : ftemp (90도), 섭씨 : ctemp

ftemp = 90.0
ctemp = ((ftemp - 32.0) * 5.0) // 9.0

print("ftemp =", ftemp, "ctemp =", ctemp)

# 숫자게임
"""
print("숫자 게임에 오신 것을 환영합니다.")
num = 62
s = input("숫자를 입력하세요.")
guess = int(s)
if num == guess:
    print("정답입니다.")
else:
    print("오답입니다.")
print("게임이 종료되었습니다.")
"""

# print() 함수 실습
"""
print("안녕하세요? 여러분")
print("저는 파이썬을 무척 좋아합니다.")
print("9*8은",9*8,"입니다.")
print("안녕히 계세요.")
"""

# 터틀 그래픽 (정사각형)
"""
import turtle
t = turtle.Pen()
t.pencolor("red")
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
"""

# 터틀 그래픽 2 (별)
"""
import turtle
t = turtle.Turtle()
for i in [0,1,2,3,4]:
    t.forward(50)
    t.right(144)
"""

# 온도 측정 (온도 = 30도, 20도 초과 = 얇은 옷을 입으세요!, 20도 미만 = 두꺼운 옷을 입으세요!)
"""
temp = 30
if temp > 20:
    print("얇은 옷을 입으세요!")
else:
    print("두꺼운 옷을 입으세요!")
"""

# While 문 (sign = stop, stop 할 동안 빙 돌고 go 하는 순간 직진) (그림 참조)
"""
sign = "stop"
while sign == "stop":
    sign = input("사인을 입력하세요")
print("OK! 출발합니다.")
"""

# 숫자 추측 게임 (숫자 = 62, 플레이어가 임의 숫자 입력, 맞으면 맞았습니다, 틀리면 틀렸습니다, 게임 종료)
"""
print("숫자 추측 게임에 오신 것을 환영합니다!")
com = 62
player = int(input("숫자를 입력하세요!"))

if com == player:
    print("맞았습니다!")
else:
    print("틀렸습니다!")
print("게임을 종료합니다.")
"""

