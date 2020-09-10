"""
a = ["철수", "영희"]
for name in a:
    print("dddd" + name)
"""

"""
sum = 0
for x in range(10):
    sum = sum + x
    print(sum)
"""

print()

"""
avg = sum // 9
print("평균 =",avg)
"""

"""
sum = 0
for x in range(0,10):
    sum = sum + x
print(sum)
"""

"""
sum = 0
for x in range(11,21):
    sum = sum + x
print(sum)
"""
"""
a = "윤상준"

for c in a:
    print(c, end = " ")
"""

"""
num = int(input("정수를 입력하시오 :"))
fact = 1
for c in range(1,num + 1):
    fact = fact * c
print("{}! = {}".format(num,fact))
"""

# Lab: 온도 변환 테이블 출력
"""
for t in range (0,101,10):
    c = (t-32.0) * 5.0 / 9.0
    print(t,"->",round(c,2))
"""

# Lab: 화면에 별 그리기
"""
import turtle

star = turtle.Turtle()

for i in range(5):
    star.forward(50)
    star.right(144)
"""

# Lab: 화면에 다각형 그리기
"""
import turtle

polygon = turtle.Turtle()

num_sides = 6
side_lenth = 70
angle = 360.0 / num_sides

for i in range(num_sides):
    polygon.forward(side_lenth)
    polygon.right(angle)
"""

# Lab: 화면에 사각형 그리기
"""
import turtle

t = turtle.Turtle()

for i in range(3):
    t.left(20)

    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
"""
"""
# While문 예제

i = 0

while i < 5:
    print("환영합니다.")
    i += 1

print("반복이 종료되었습니다.")
"""
# Lab: 반복
"""
i = 0

while i < 10:
    print(i,end = " ")
    i += 1
"""

# Lab: (1+2+3+...+9+10) 계산하기
# (1+2+3+...+9+10)의 값을 계산하는 프로그램을 작성하여 보자.
# 이것은 공식으로도 계산할 수 있으나 우리는 반복 구조를 사용해보자.
"""
i = 1
sum = 0
while i < 11:
    sum += i
    i += 1
print("합계 =",sum)
"""

# Lab: 팩토리얼 계산
# 팩토리얼을 계산하는 프로그램을 작성하여 보자.
# 팩토리얼 n!은 1부터 n까지의 정수를 모두 곱한 것을 의미한다.
# 즉, n! = 1×2×3×……×(n-1)×n이다.
# 예를 들어서 10!을 계산하는 프로그램을 작성하여 보자.
"""
i = 1
n = 1
while i < 11:
    n *= i
    i += 1
print("10!은",n,"입니다!")
"""

# Lab: (1+2+3+...+9+10) 계산하기
# (1+2+3+...+9+10)의 값을 계산하는 프로그램을 작성하여 보자.
# 이것은 공식으로도 계산할 수 있으나 우리는 반복 구조를 사용해보자.
# 3*1 = 3
# 3*2 = 6
# 3*3 = 9
# 3*4 = 12
# 3*5 = 15
# 3*6 = 18
# 3*7 = 21
# 3*8 = 24
# 3*9 = 27
"""
i = 1
while i < 10:
    print("3 * %d = %d"%(i,3*i))
    i += 1
"""

# Lab: 배수의 합 계산 프로그램
# 1부터 100사이의 모든 3의 배수의 합을 계산하여 출력하는 프로그램을 반복 구조를 사용하여 작성하라.
# 1부터 100 사이의 모든 3의 배수의 합은 1683입니다.
"""
sum = 0
n = 1

while n <= 100:
    if n % 3 == 0:
        sum += n
    n += 1
print("1부터 100 사이의 모든 3의 배수의 합은",sum,"입니다.")
"""

# Lab: 자리수의 합
# 정수 안의 각 자리수의 합을 계산하는 프로그램을 작성해보자.
# 예를 들어서 1234라면 (1+2+3+4)를 계산하는 것이다.
# 자리수의 합은 10입니다.
"""
number = 1234
sum = 0;
while number > 0 :
    digit = number % 10
    sum = sum + digit
    number = number // 10
print("자리수의 합은 %d입니다." % sum)
"""

# 보초값(sentinel) 사용하기
# 사용자로부터 임의의 개수의 성적을 받아서
# 평균을 계산한 후에 출력하는 프로그램 을 작성하여 보자.
# 센티널로는 음수의 값을 사용하자.
# 종료하려면 음수를 입력하시오
# 성적을 입력하시오: 10
# 성적을 입력하시오: 20
# 성적을 입력하시오: 30
# 성적을 입력하시오: -1
# 성적의 평균은 20.000000입니다.
"""
n = 0
sum = 0
score = 0

print("종료하려면 음수를 입력하시오")

while score >= 0 :
    score = int(input("성적을 입력하시오: "))
    if score > 0:
        sum = sum + score
        n = n + 1

# 평균을 계산하고 화면에 출력한다.
if n > 0 :
    average = sum / n
print("성적의 평균은 %f입니다." % average)
"""

# Lab: 숫자 맞추기 게임
# 앞에 등장하였던 숫자 맞추기 게임 업그레이드
# 1부터 100 사이의 숫자를 맞추시오
# 숫자를 입력하시오: 50
# 낮음!
# 숫자를 입력하시오: 75
# 낮음!
# 숫자를 입력하시오: 82
# 낮음!
# 숫자를 입력하시오: 91
# 높음!
# 숫자를 입력하시오: 86
# 낮음!
# 숫자를 입력하시오: 87
# 축하합니다. 시도횟수= 6
"""
import random

tries = 0
number = random.randint(1, 100)

print("1부터 100 사이의 숫자를 맞추시오")

while tries < 10:
    guess = int(input("숫자를 입력하시오: "))
    tries = tries + 1
    if guess < number:
        print("낮음!")
    elif guess > number:
        print("높음!")
    else:
        break

if guess == number:
     print("축하합니다. 시도횟수=", tries)
else:
     print("정답은 ", number)
"""

# 중첩 루프 예제
"""
for y in range(5):
    for x in range(10):
        print("*",end = "")
    print("")
"""

# Lab: 피타고라스 삼각형 찾기
# 피타고라스의 정리는 직각 삼각형에서 직각을 낀 두 변의 길이를 a, b라고 하고,
# 빗변의 길이를 c라고 하면 의 수식이 성립한다는 것이다.
# 각 변의 길이가 100보다 작은 삼각형 중에서
# 피타고라스의 정리가 성립하는 직각 삼각형은 몇 개나 있을까?
"""
for a in range(1, 101, 1):
    for b in range(1, 101, 1):
        for c in range(1, 101, 1):
            if( (a*a+b*b)==c*c ):
                print(a, b, c)
"""

# 예제
# 문자열을 받아서 모음을 전부 없애는 코드는 다음과 같이 작성할 수 있다.
# 문자열을 입력하시오: kkkoommm
# kkkmmm
"""
s = input("문자열을 입력하시오.")
vowels = "aeiouAEIOU"
result = ""

for letter in s:
    if letter not in vowels:
        result += letter
print(result)
"""

# 예제
# 문자열 중에서 자음과 모음의 개수를 집계하는 프로그램을 작성하여 보자.
# 문자열을 입력하시오: iokkk
# 모음의 개수 2
# 자음의 개수 3
"""
original = input("문자열을 입력하시오:")
vowels = 0
consonants = 0
word = original.lower()

if len(original) > 0 and original.isalpha():
    for char in original:
        if char in "aeiouAEIOU":
            vowels += 1
        else:
            consonants += 1
print("모음의 개수",vowels)
print("자음의 개수",consonants)
"""

# Lab: 문자열 조사
# 문자열을 조사하여서 알파벳 문자의 개수, 숫자의 개수,
# 스페이스의 개수를 출력하는 프로그램을 작성하라.
# 문자열을 입력하시오: Meav-01-I Dreamt I Dwelt In Marble Halls-192k.mp3
# 알파벳 문자의 개수= 33
# 숫자 문자의 개수= 6
# 스페이스  문자의 개수= 6
"""
statement = input("문자열을 입력하시오:")
alphas = 0
digits = 0
spaces = 0

for c in statement:
    if c.isalpha():
        alphas += 1
    if c.isdigit():
        digits += 1
    if c.isspace():
        spaces += 1
print ("알파벳 문자의 개수=", alphas)
print ("숫자 문자의 개수=", digits)
print ("스페이스  문자의 개수=", spaces)
"""

# Lab: 계좌번호 처리
# 인터넷 뱅킹을 사용하다보면 계좌번호를 입력할 때,
# "312-02-1234567"과 같이 "-"을 사용하면 안 된다는 경고를 받는다.
# 사용자로부터 "-"가 포함된 계좌 번호를 받아서 "-"을 삭제한 문자열을 만들어보자.
# 계좌번호를  입력하시오: 312-02-1234567
# 312021234567
"""
raw = input("계좌번호를 입력하시오:")
processed = ""
for c in raw:
    if c != "-":
        processed += c
print(processed)
"""