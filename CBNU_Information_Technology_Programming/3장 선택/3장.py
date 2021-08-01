"""
# 수화물 무게

weight = int(input("짐의 무게는 얼마입니까? :"))

if weight < 20:
    print("짐에 대한 수수료는 없습니다.")
    print("감사합니다.")
elif weight > 20:
    print("무거운 짐은 20,000원을 내셔야 합니다.")
    print("감사합니다.")
"""

"""
# 짝수 홀수 계산
num = int(input("정수를 입력하시오. :"))
if (num % 2) == 0:
    print("입력된 정수는 짝수입니다.")
else:
    print("입력된 정수는 홀수입니다.")
"""

"""
# 정수 중 큰 수 계산
num1 = int(input("첫 번째 정수 :"))
num2 = int(input("두 번째 정수 :"))

if num1 > num2:
    print("큰 수는 {}".format(num1))
if num2 > num1:
    print("큰 수는 {}".format(num2))
"""
"""
# 인터넷 쇼핑몰

price = int(input("구입 금액을 입력하시오. :"))
if price > 100000:
    discount = price * 0.05
    total_price = price - discount
    print("할인 금액 :", discount)
    print("지불 금액 :", total_price)
else:
    print("지불 금액 :", price)
"""
"""
word = input("문자열을 입력하시오. :")
length = len(word)
if (length % 2) == 1:
    word1 = (length // 2)
    print("중앙 글자는",word[word1])
else:
    word2 = (length // 2 - 1)
    word3 = (length // 2)
    print("중앙 글자는",word[word2],word[word3])
"""
"""
num = float(input("이수한 학점수를 입력하시오. :"))
score = float(input("평점을 입력하시오. :"))

if num >= 140 and score >= 2.0:
    print("졸업이 가능합니다!")
else:
    print("졸업이 힘듭니다!")
"""
"""
num = int(input("정수를 입력하시오. :"))

if num > 0:
    print("입력된 정수는 양수입니다.")
elif num < 0:
    print("입력된 정수는 음수입니다.")
else:
    print('입력된 정수는 0 입니다.')
"""
"""
# if else
"""
"""
list = ["hong","yoon"]
id = input("아이디를 입력하시오 :")

if id in list:
    pw = input("패스워드를 입력하시오 :")
    if pw == 12345:
        print("환영합니다.")
    else:
        print("패스워드가 다릅니다.")
else:
    print("등록되지 않은 아이디 입니다.")
"""
"""
month = int(input("월을 입력하시오 :"))
if month == 12:
    day12 = 31
    print("월의 날수는",day12)
elif month == 5:
    day5 = 27
    print("월의 날수는",day5)
else:
    print("잘못된 입력입니다.")
"""
"""
# 윤년 계산기

year = int(input("연도를 입력하시오. :"))
if (year % 4 == 0) or (year % 400 == 0) and (year % 100 != 0):
    print("{}년은 윤년입니다.".format(year))
else:
    print("{}년은 평년입니다.".format(year))
"""
"""
# 이차 방정식 (복습 필요)
import math
import math

A = float(input("A = "))
B = float(input("B = "))
C = float(input("C = "))

D = B * B - 4 * A * C   # d = b^2 - 4ac
if A == 0:
    print ("x=", -C/B)
if D == 0:
    print ("x =", -B / (2.0 * A))
elif D > 0:
    print ("x1 =", (-B + math.sqrt(D)) / (2.0 * A))
    print ("x2 =", (-B - math.sqrt(D)) / (2.0 * A))
else:
    print ("실근이 존재하지 않음")
"""
"""
# 숫자 맞추기 게임
import random
com = random.randint(1,100)
print("숫자 게임에 오신 것을 환영합니다.")
while True:
    player = int(input("숫자를 맞춰 보세요. :"))
    if player > com:
        print("너무 큼!")
    elif player < com:
        print("너무 작음!")
    else:
        print("정답입니다.")
        print("게임 종료")
        break
"""
# 가위 바위 보 게임
import random

player = input("(가위, 바위, 보) 중에서 하나를 선택하세요: ")

number = random.randint(0,2)
if (number == 0):
    computer = "가위"
elif (number == 1):
    computer = "바위"
else:
    computer = "보"
print("사용자: ", player, "컴퓨터: ", computer)

if (player == computer):
    print("비겼음!");
elif (player == "바위"):
    if (computer == "보"):
        print("컴퓨터가 이겼음!");
    else:
        print("사용자가 이겼음!");
elif (player == "보"):
    if (computer == "비위"):
        print("사용자가 이겼음!");
    else:
        print("컴퓨터가 이겼음!");
elif (player == "가위"):
    if (computer == "바위"):
        print("컴퓨터가 이겼음!");
    else:
        print("사용자가 이겼음!");

