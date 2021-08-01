# 곱하기 함수
"""
def get_multi(start,end):
    multi = 1
    for i in range(start,end+1):
        multi *= i
    return multi

value = get_multi(1,10)
print(value)
"""

"""
square(side)			// 정수를 제곱하는 함수
compute_average(list)		// 평균을 구하는 함수
set_cursor_type(c)		// 커서의 타입을 설정하는 함수
"""

# 예제
"""
def get_sum(start,end):
    sum = 0
    for i in range(start,end+1):
        sum += i
    return sum

value1 = get_sum(1,10)
value2 = get_sum(1,20)

print(value1)
print(value2)
"""

# 예제 2
"""
def square(n):
        return(n*n)
print(square(10))
"""

# 예제 3
"""
def get_max(num1,num2):
    if num1 > num2:
        print(num1)
    elif num1 < num2:
        print(num2)
    return max

value3 = get_max(20,30)
print(value3)
"""

# 함수 작성의 예 #2
# 정수의 거듭제곱값을 계산하여 반환하는 함수를 작성하여 보자. (파이썬에는 ** 연산자가 있지만)
"""
def power(x,y):
    result = 1
    for i in range(y):
        result = result * x
    return result

print(power(10,2))
"""
"""
print(power(10, 2))

def power(x, y):
	result = 1
	for i in range(y):
		result = result * x
	return result

# 함수 정의가 먼저 와야 한다.
"""
"""
def main():
	print(power(10, 2))

def power(x, y):
	result = 1
	for i in range(y):
		result = result * x
	return result  

main()

# 이 경우는 가능하다. main함수를 마지막에 출력했기에 main함수, px`ower함수 모두가 정의되어 있다고 볼 수 있다.
"""

# Lab: 생일 축하 함수
"""
def happybirthday():
    print("생일축하 합니다 !")
    print("생일축하 합니다 !")
    print("사랑하는 친구의 생일축하 합니다 !")
    return happybirthday

print(happybirthday())
"""

# Lab: 온도 변환 함수
# 섭씨 온도를 화씨 온도로 변환하여 반환하는 함수 FtoC()를 작성하고 테스트하라.
# 화씨온도를 입력하시오: 32.0
# 0.0
"""
def Ftoc(temp_f):
    temp_c = 5.0 * ((temp_f - 32.0))/9.0
    return temp_c

temp_f = float(input("화씨온도를 입력하시오."))

print(Ftoc(temp_f))
"""

# Lab: 소수 찾기
# 소수를 판별하는 함수 is_prime()을 작성하여 사용하여 보자.
"""
def is_prime(n):
    for i in range(2,n):
        if (n%i == 0):
            return False
    return True

n = int(input("정수를 입력하시오 :"))
print(is_prime(n))
"""

# 구의 부피
# 구의 부피를 계산하는 함수 sphereVolume()을 작성하여 보자. 반지름이 r인 구의 부피는 다음과 같다.
# V = 4/3 * 파이 * r^3
# 구의 반지름을 입력하시오: 10.0
# 4188.790204786391
"""
import math
def sphereVolume(r):
    volume = 4.0 / 3.0 * math.pi * (r ** 3)
    return volume

print(sphereVolume(10))
"""
# Lab: 패스워드 생성기
# 일회용 패스워드 생성기를 이용하여서 3개의 패스워드를 생성하여 출력하는 프로그램을 작성해보자.
# q546zv
# 1kvkss
# b3vrmi

import random

def get_password():
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    password = ""

    for i in range(3):
        index = random.randrange(len(alphabet))
        index2 = random.randrange(-10,0)
        password = password + alphabet[index] + alphabet[index2]
    return password

print(get_password())
print(get_password())
print(get_password())


# 디폴트 인수
"""
def greet(name, msg = "별일없죠?"):
    print("안녕",name,msg)
    return greet

print(greet("상준"))
"""

# Lab: 패스워드 생성기
# 사칙 연산을 수행하는 4개의 함수(add(), sub(), mul(), div())를 작성한다.
# 이들 함수를 이용하여 10+20*30을 계산하여 보자. 함수를 호출할 때 키워드 인수를 사용하여 호출해보자.
"""
def add(x,y):
    return(x+y)

def sub(x,y):
    return(x-y)

def mul(x,y):
    return(x*y)

def div(x,y):
    return(x/y)

print(add(10,(mul(20,30))))
"""

# Lab: 온도변환기
# 섭씨 온도를 화씨 온도로, 또 그 반대로 변환하는 프로그램을 작성하여 보자.
#  'c' 섭씨온도에서 화씨온도로 변환
#  'f' 화씨온도에서 섭씨온도로 변환
#  'q' 종료
# 메뉴에서 선택하세요.c
# 섭씨온도: 100
# 화씨온도: 212.0
#  'c' 섭씨온도에서 화씨온도로 변환
#  'f' 화씨온도에서 섭씨온도로 변환
#  'q' 종료
# 메뉴에서 선택하세요.
"""
def printOptions():
    print( " 'c' 섭씨온도에서 화씨온도로 변환")
    print( " 'f' 화씨온도에서 섭씨온도로 변환")
    print( " 'q' 종료")

def C2F(c_temp):
    return 9.0 / 5.0 * c_temp + 32

def F2C(f_temp):
    return (f_temp - 32.0) * 5.0 / 9.0

printOptions()
choice = input("메뉴에서 선택하세요.")
while True:
    if choice == "c":
        temp = float( input("섭씨온도: "))
        print ("화씨온도:", C2F(temp))
    elif choice == "f":
        temp = float(input("화씨온도: "))
        print ("섭씨온도:", F2C(temp))
    elif choice == "q":
        print("종료합니다.")
        break
    printOptions()
    choice = input("메뉴에서 선택하세요.")
"""

# 값에 의한 호출 1
"""
def modify1(s):
	s += "To You"
    

msg = "Happy Birthday"
print("msg=", msg)
modify1(msg)
print("msg=", msg)
"""

# 값에 의한 호출 2
"""
def modify2(li):
    li += [100,200]

list = [1,2,3,4,5]
print(list)
modify2(list)
print(list)
"""

# 전역 변수 : 함수 외부에 있는 변수
# 지역 변수 : 함수 내부에 있는 변수

# 지역 변수
"""
def sub():
	s = "바나나가 좋음!"
	print(s)

sub()
"""

# 전역 변수
"""
def sub():
	print(s)

s = "사과가 좋음!"
sub()
"""

# 전역 변수를 함수 안에서 사용하려면
"""
def sub():
	global s

	print(s)
	s = "바나나가 좋음!"
	print(s)

s = "사과가 좋음!"
sub()
print(s)
"""

# 예제
"""
def sub(x, y):
    global a

    a = 7
    x,y = y,x
    b = 3
    print(a, b, x, y)

a,b,x,y = 1,2,3,4
sub(x, y)
print(a, b, x, y)
"""

# Lab: 매개변수 = 지역변수
"""
# 함수가 정의된다.
def sub( mylist ):
   # 리스트가 함수로 전달된다. 
   mylist = [1, 2, 3, 4]   # 새로운 리스트가 매개변수로 할당된다. 
   print ("함수 내부에서의 mylist: ", mylist)
   return

# 여기서 sub() 함수를 호출한다. 
mylist = [10, 20, 30, 40];
sub( mylist );
print ("함수 외부에서의 mylist: ", mylist)
"""

# Lab: 상수
# 파이를 전역 변수로 선언하고 이것을 이용하여서 원의 면적과 원의 둘레를 계산하는 함수를 작성해보자.
# 원의 반지름을 입력하시오: 10
# 원의 면적: 314.159265358979
# 원의 둘레: 62.8318530717958
"""
pi = 3.14159265358979

def main():
    r = float(input("원릐 반지름을 입력하시오 :"))
    print("원의 면적 :",circlearea(r))
    print("원의 둘레 :",circleCircumference(r))

def circlearea(r):
    return pi * r * rㅍ

def circleCircumference(r):
    return 2 * pi * r

print(main())
"""

# 무명 함수
# 무명 함수는 이름은 없고 몸체만 있는 함수이다. 파이썬에서 무명 함수는 lambda 키워드로 만들어진다.
"""
sum = lambda x, y: x+y

print( "정수의 합  : ", sum( 10, 20 ))
print( "정수의 합  : ", sum( 20, 20 ))
"""

# 피보나치 수열 모듈
"""
def fib(n):    # 피보나치 수열을 화면에 출력한다.
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()
"""
"""
import fibo	# 이 경우에는 세부 함수를 일일이 지정해줘야함.

fibo.fib(1000)

fibo.__name__
'fibo’
"""
# 함수를 사용한 프로그램 설계
# 문제를 한 번에 해결하려고 하지 말고 더 작은 크기의 문제들로 분해한다. 문제가 충분히 작아질 때까지 계속해서 분해한다.
# 문제가 충분히 작아졌으면 각각의 문제를 함수로 작성한다.
# 이들 함수들을 조립하면 최종 프로그램이 완성된다.

