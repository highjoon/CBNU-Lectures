print("윤상준")
print("hello world")
print("안녕하세요")

print()

print(2+3)  # idle 에서는 print() 필요 없음
print(2-3)
print(2*3)
print(2/3)
print(2//3)
print(2%3)

print()

print("결과값은",2*7,"입니다.")
print("2 곱하기 7의 결과값은",2*7,"입니다.")

print()

# 온도 변환 프로그램
# 화씨 온도 -> 섭씨 온도
ftemp = 90.0
ctemp = (ftemp - 32.0) * 5.0 // 9.0

print("ftemp =",ftemp,",","ctemp =",ctemp)

# 숫자게임
"""
print("숫자게임에 오신 것을 환영합니다.")
number = 62
s = input("숫자를 입력하세요.")
guess = int(s)
if guess == number:
    print("정답입니다.")
else:
    print('오답입니다.')
print("게임이 종료되었습니다.")
"""

# print() 함수 실습
"""
print("안녕하세요? 여러분")
print("저는 파이썬을 무척 좋아합니다.")
print("9*8은",9*8,"입니다.")
print("안녕히 계세요.")
"""

# 터틀 그래픽
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

# 터틀 그래픽 2
"""
import turtle

t = turtle.Turtle()

for i in [0,1,2,3,4]:
    t.forward(50)
    t.right(144)
"""

# 온도 측정
"""
temp = 30
if temp > 20:
    print("얇은 옷을 입으세요!")
else:
    print("두꺼운 옷을 입으세요!")
"""

# While 문
"""
sign = "stop"

while sign == "stop":
    sign = input("현재 신호를 입력하세요 : ")
print("ok! 진행합니다.")
"""

# 숫자 추측 게임
"""
print("숫자게임에 오신 것을 환영합니다.")
num = 62
a = int(input("1부터 100사이의 숫자를 추측해보세요: "))
if a == num:
    print("맞았습니다.")
print("게임이 종료되었습니다.")
"""
