# 순서도 그리기 파악.

# Lab: 터틀 그래픽
# 사용자로부터 명령어를 받아서 터틀을 제어해보자.
# 즉 사용자가 "left"를 입력하면 왼쪽으로 회전하게 하고 사용자가 "right"를 입력하면 오른쪽으로 회전하게 하자.
# 왼쪽=left, 오른쪽=right:left
# 왼쪽=left, 오른쪽=right:right
# 왼쪽=left, 오른쪽=right:left
# 왼쪽=left, 오른쪽=right:right
# 왼쪽=left, 오른쪽=right:
# 왼쪽,오른쪽 = 60 / 전진 = 50
"""
import turtle
t = turtle.Pen()

while True:
    direction = input("왼쪽 = left, 오른쪽 = right 중 하나를 입력하시오.")
    if direction == "left":
        t.left(60)
        t.forward(50)
    if direction == "right":
        t.right(60)
        t.forward(50)
"""

# Lab: 수하물 비용 계산
# 항공사에서는 짐을 부칠 때, 20kg이 넘어가면 20,000원을 내야한다고 하자.
# 20kg 미만이면 수수료는 없다. 사용자로부터 짐의 무게를 입력받고 사용자가 지불하여야 할 금액을 계산하는 프로그램을 작성해보자.
# 짐의 무게는 얼마입니까? 18
# 짐에 대한 수수료는 없습니다.
# 감사합니다.
# 짐의 무게는 얼마입니까? 30
# 무거운 짐은 20,000원을 내셔야 합니다.
# 감사합니다.
"""
weight = int(input("짐의 무게는 얼마입니까?"))
if weight < 20:
    print("짐에 대한 수수료는 없습니다.")
else:
    print("무거운 짐은 20,000원을 내셔야 합니다.")
print("감사합니다.")
"""


# 짝수 홀수 계산
# 키보드에서 입력받은 정수가 홀수인지 짝수인지를 말해주는 프로그램을 작성하여 보자. 홀수와 짝수는 어떻게 구별할 수 있는가?
# 정수를 입력하시오: 2
# 입력된 정수는 짝수입니다.
"""
num = int(input("정수를 입력하세요."))
if num % 2 == 0:
    print("해당 정수는 짝수입니다.")
else:
    print("해당 정수는 홀수입니다.")
"""

# 정수 중 큰 수 계산
# 사용자로부터 두개의 정수를 입력받아서 둘 중에서 큰 수를 출력하는 프로그램을 작성하여 보자.
# 첫 번째 정수: 10
# 두 번째 정수: 20
# 큰 수는 20
"""
num1 = int(input("첫 번째 정수 :"))
num2 = int(input("두 번째 정수 :"))

if num1 > num2:
    max = num1
else:
    max = num2
print("큰 수는",max)
"""


# 인터넷 쇼핑몰
# 인터넷 쇼핑몰에서 물건을 구입할 때, 구입액이 10만원 이상이면 5%의 할인을 해준 다고 하자.
# 사용자에게 구입 금액을 물어보고 최종적으로 할인 금액과 지불 금액을 출력하는 프로그램을 작성해보자.
# 구입 금액을 입력하시오: 100500
# 지불 금액은  95475.0 입니다.
"""
price = int(input("구입 금액을 입력하시오 :"))
if price > 100000:
    discount = 0.05
    sales = price - (price * discount)
print("지불 금액은", sales, "입니다.")
"""
# Lab: 문자열의 중간문자
# 문자열의 중앙에 있는 문자를 출력한다.
# 예를 들어서 문자열이 "weekday"이라면 중앙의 문자는 "k"가 된다.
# 하지만 만약 문자열이 짝수개의 문자를 가지고 있다면 중앙의 2개의 글자를 출력한다.
# 예를 들어서 "string" 문자열에서는 "ri"를 반환한다.
# 문자열을 입력하시오: weekday
# 중앙글자는  k
# 문자열을 입력하시오: string
# 중앙글자는  r i
# 리스트 사용
"""
word = input("문자열을 입력하시오. :")
length = len(word)

if length % 2 != 0:
    ch1 = word[length//2]
    print("중앙 글자는",ch1)
else:
    ch2 = word[length//2-1]
    ch3 = word[length//2]
    print("중앙글자는 ",ch2,ch3,sep="")
"""
# Lab: 졸업 학점 검사하기
# 어떤 대학교를 졸업하려면 적어도 140학점을 이수해야 하고 평점이 2.0은 되어야 한 다고 하자.
# 이것을 파이썬 프로그램으로 검사해보자.
# 사용자에게 이수학점수와 평점 을 물어보고 졸업 가능 여부를 출력하는 프로그램을 작성해보자.
# 이수한 학점수를 입력하시오: 120
# 평점을 입력하시오: 2.3
# 졸업이 힘듭니다!
"""
credits = float(input("이수한 학점수를 입력하시오. :"))
gpa = float(input("평점을 입력하시오. :"))

if credits > 140 and gpa > 2.0:
    print("졸업이 가능합니다!")
else:
    print("졸업이 힘듭니다!")
"""

# Lab: 음수, 0, 양수 구별하기
# 사용자로부터 정수를 받아서 음수, 0, 양수 중의 하나로 분류하여 보자.
# 정수를 입력하시오: -10
# 입력된 정수는 음수입니다.
# 정수를 입력하시오: 0
# 입력된 정수는 0입니다.
"""
num = int(input("정수를 입력하시오. :"))

if num > 0:
    print("입력된 정수는 양수입니다.")
elif num < 0:
    print("입력된 정수는 음수입니다.")
else:
    print('입력된 정수는 0 입니다.')
"""

# if else
# 예를 들어보자. 마트에서 사과가 신선하면 사과를 사기로 한다.
# 만약 사과가 개당 1000원 미만이면 10개를 산다. 하지만 사과가 개당 1000원 이상이면 5개만 산다.
"""
appleQuality = input("사과의 상태를 입력하시오 :")
applePrice = int(input("사과 1개의 가격을 입력하시오 :"))
if appleQuality == "신선":
    if applePrice < 1000:
        print("10개를 산다.")
    else:
        print("5개를 산다.")
else:
    print("사과를 사지 않는다.")

"""

# Lab: 아이디 검사
# 아이디를 입력받아서 등록된 아이디인지를 검사하는 프로그램을 작성해보자.
# 등록된 아이디를 리스트(list)에 저장하도록 한다. 아이디가 일치하면 패스워드 물어본다.
# 아이디를 입력하시오: hong
# 패스워드를 입력하시오: 12345678
# 환영합니다.
"""
id_list = ["hong","Yoon","Park","Lee"]
id = input("아이디를 입력하세요.")
if id in id_list:
    pw = int(input("패스워드를 입력하세요."))
    if pw == 12345:
        print("환영합니다.")
    else:
        print("잘못된 패스워드 입니다.")
else:
    print("등록되지 않은 아이디 입니다.")
"""

# Lab: 달의 일수 출력
# 1년의 각 달의 일수를 출력하는 프로그램을 작성하여보자.
# 즉 특정 달이 입력되면 그 달의 일수를 출력한다.
# 여러 가지 방법으로 작성할 수 있겠으나 여기서는 if-else 문을 사용하여 보자.
# 월을 입력하시오:12
# 월의 날수는 31
# 2월 = 29일, 4,6,10월 = 30일, 나머지 31일
"""
month = int(input("월을 입력하시오."))
if month == 2:
    print("월의 날수는 29일")
elif month == 2 or month == 6 or month == 10:
    print("월의 날수는 30일")
else:
    print("월의 날수는 31일")
"""

# 윤년 계산기
# 입력된 연도가 윤년인지 아닌지를 판단하는 프로그램을 만들어보자. 윤년은 다음의 조건 을 만족해야 한다.
# 연도가 4로 나누어 떨어지면 윤년이다.
# 100으로 나누어 떨어지는 연도는 제외한다.
# 400으로 나누어 떨어지는 연도는 윤년이다.
# 연도를 입력하시오: 2012
# 2012 년은 윤년입니다.
"""
year = int(input("연도를 입력하시오 :"))
if (year % 4 == 0 or year % 400 == 0) and year % 100 != 0:
    print("윤년입니다.")
else:
    print("평년입니다.")
"""

# 이차 방정식 (복습 필요)
# 이차 방정식은 추억의 방정식일 것이다. 고등학교에서 아마 가장 중점적으로 학습한 내용이 아닐까 생각된다.
# 이차 방정식 ax^2 + bx + c = 0 의 근을 계산하는 프로그램을 작성하여 보자.
# A = 1
# B = -5
# C = 6
# x^2 -5x + 6 = 0
# 근 = B^2 - 4AC
# x1 = 3.0
# x2 = 2.0
"""
from math import *
A = float(input("A ="))
B = float(input("B ="))
C = float(input("C ="))

D = B**2 - 4*A*C
if A == 0:
    print("X = ", -C/B)
if D == 0:
    print("X = ", -B/(2.0 * A))
elif D > 0:
    print("x1 = ", -B + sqrt(D)/(2.0*A))
    print("x2 = ", -B - sqrt(D)/(2.0*A))
else:
    print("실근이 존재하지 않음")
"""

# 숫자 맞추기 게임
# 이 예제는 프로그램이 가지고 있는 정수를 사용자가 알아맞히는 게임이다.
# 사용자가 답을 제시하면 프로그램은 자신이 저장한 정수와 비교하여 제시된 정수가 더 높은지 낮은지 만을 알려준다.
# 정수의 범위를 1부터 100까지로 한정하도록 하자. 그리고 사용자는 단 한 번의 기회만 가진다.
# 숫자 게임에 오신 것을 환영합니다.
# 숫자를 맞춰 보세요: 9
# 너무 큼!
# 게임 종료
"""
import random
print("숫자 게임에 오신 것을 환영합니다.")
com = random.randint(1,100)
player = int(input("숫자를 맞춰 보세요 :"))
if player > com:
    print("너무 큼!")
elif player < com:
    print("너무 작음!")
else:
    print("정답입니다!")
print("게임 종료")
"""

# 개인적 반복문 연습

"""
import random
com = random.randint(1,100)
print("숫자 게임에 오신 것을 환영합니다.")
cnt = 0
for i in range(4):
    cnt += 1
    player = int(input("숫자를 맞춰 보세요 :"))
    if player > com:
        print("너무 큼!")
    elif player < com:
        print("너무 작음!")
    else:
        print("정답입니다!")
        print("게임 종료")
        break
print("패배하였습니다!")
"""

# Lab: 가위 바위 보
# 사용자가 가위, 바위, 보 중에서 하나를 선택하고 컴퓨터도 난수로 가위, 바위, 보 중에서 하나를 선택한다.
# 사용자의 선택과 컴퓨터의 선택을 비교하여서 승패를 화면에 출력한다.
# (가위, 바위, 보) 중에서 하나를 선택하세요: 가위
# 사용자:  가위 컴퓨터:  바위
# 컴퓨터가 이겼음!
"""
import random
com = random.randint(0,2)
player = input("가위, 바위, 보 중 하나를 입력하세요 :")

if com == 0:
   com_pick = "가위"
elif com == 1:
    com_pick = "바위"
else:
    com_pick = "보"

print("플레이어 :",player,",","컴퓨터 :",com_pick)

if player == "가위":
    if com == 1:
        print("컴퓨터가 승리했습니다.")
    elif com == 2:
        print("플레이어가 승리했습니다.")
    else:
        print("비겼습니다.")
elif player == "바위":
    if com == 2:
        print("컴퓨터가 승리했습니다.")
    elif com == 0:
        print("플레이어가 승리했습니다.")
    else:
        print("비겼습니다.")
elif player == "보":
    if com == 0:
        print("컴퓨터가 승리했습니다.")
    elif com == 1:
        print("플레이어가 승리했습니다.")
    else:
        print("비겼습니다.")
"""