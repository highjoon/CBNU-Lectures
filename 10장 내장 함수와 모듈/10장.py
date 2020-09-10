# abs(x)함수
# 절댓값
# 인자는 정수 또는 실수
# 인자가 복소수면 그 크기가 반환
"""
print(abs(-3))
print(abs(3+4j))
"""

# chr(i) 함수
# 숫자를 넣으면 문자로 변환.
# 유니코드 문자표 기준 (아스키 문자표)
"""
print(chr(65))
print(ord('A'))
"""

# complie(source, filename, mode) 함수
"""
with open('mymodule.py') as f:
	lines = f.read

code_obj = compile(lines, 'mymodule.py', 'exec')
exec(code_obj)
"""


# complex(real, imag) 함수
# 복소수 출력 함수
"""
x = complex(4,2)
print(x)
"""

# dir 함수
# dir은 객체가 갖고있는 변수나 함수를 보여준다.
"""
print(dir([1,2,3]))
"""

# eval() 함수
# eval()은 파이썬의 수식을 문자열로 받아서 실행하고
# 그 결과를 반환한다.
"""
print(eval('1+2'))
x=1
y=1
print(eval('x+y'))

eval("print('hi')")
"""

# exec() 함수
# exec() 함수는 수식뿐만 아니라 모든 파이썬 문장을 받아서 실행한다.
"""
exec('y=2+3')
print(y)

statements = \"""
import math
def area_of_circle(radius):
	return math.pi * radius * radius
\"""

exec(statements)
print(area_of_circle(5))
"""

# float() 함수
# float() 함수는 문자열을 부동소수점수로 변환하는 기능을 한다.
# 실수 12.345 받은 후 float 변형
"""
str = input('실수:')
print(str)
print(type(str))
value = float(str)
print(value)
print(type(value))
"""

# max() 함수
# max() 함수는 리스트나 튜플, 문자열에서 가장 큰 항목을 반환한다.
# 리스트 1,2,3,4,5를 values 변수로 저장 후 최고, 최저치 프린트
"""
values = [1,2,3,4,5]
print(max(values))
print(min(values))
"""

# 파이썬에서 정렬하기
# 4,2,3,5,1 정렬 (sorted, sort() 사용)
"""
values = [1,2,3,4,5]
print(sorted(values))
mylist = [1,2,3,4,5]
mylist.sort()
print(mylist)
"""

# key 매개변수
# 정렬을 하다보면 정렬에 사용되는 키를 개발자가 변경해주어야하는 경우가 종종 있다.
# sorted 정렬
# "The health know not of their health, but only the sick" 를 단어별로 쪼갠 후 정렬
#     ('홍길동',3.9, 20160303)
#     ('김철수', 3.0, 20160302)
#     ('최자영', 4.3, 20160301)
# students 리스트에 저장 후, lambda 사용 해서 학번으로 정렬
"""
print(sorted("The health know not of their health, but only the sick". split(), key = str.lower))

students = [('홍길동',3.9,20160303),
			('김철수',3.0,20160302),
			('최자영',4.3,20160301)]
print(sorted(students, key = lambda student: student[2]))
"""

# 예제
"""
class Student:
	def __init__(self, name, grade, number):
		self.name = name
		self.grade = grade
		self.number = number
	def __repr__(self):
		return repr((self.name, self.grade, self.number))

students = [Student('홍길동',3.9,20160303),
			Student('김철수',3.0,20160302),
			Student('최자영',4.3,20160301)]

print(sorted(students, key=lambda student: student.number, reverse = False))


# 오름차순 정렬과 내림차순 정렬
print(sorted(students, key = lambda student: student.number, reverse = True))
"""

# Lab: 키를 이용한 정렬 예제
# 주소록을 작성한다고 하자.
# 간단하게 사람들의 이름과 나이만 저장하고자 한다.
# 사람을 Person 이라는 클래스로 나타낸다.
# Person 클래스는 다음과 같은 인스턴스 변수를 가진다.
# name – 이름을 나타낸다.(문자열)
# age – 나이를 나타내낸다.(정수형)
# 나이순으로 정렬하여 보여주는 프로그램을 작성하자.
# 정렬의 기준의 사람의 나이이다.
# 홍길동 20, 김철수 35, 최자영 38
# [<이름: 홍길동, 나이: 20>, <이름: 김철수, 나이: 35>, <이름: 최자영, 나이: 38>]
"""
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def __repr__(self):
		return ("<이름: %s, 나이: %s>" % (self.name, self.age))

def keyage(Person):
	return Person.age

people = [Person('홍길동',20), Person('김철수',35), Person('최자영',38)]
print(sorted(people, key=keyage))
"""

# 이터레이터
# 파이썬에서는 for 루프와 함께 사용할 수 있는
# 여러 종류의 객체가 있으며 이들 객체는
# 이터러블 객체 (iterable object)이라고 불린다.
# 객체가 이터러블 객체가 되려면
# __iter__ ()은 이터러블 객체 자신을 반환한다.
# __next__ ()은 다음 반복을 위한 값을 반환한다.
# 만약 더 이상의 값이 없으면 StopIteration 예외를 발생하면 된다.
"""
class Mycounter:
	def __init__(self,current,high):
		self.current = current
		self.high = high
	def __iter__(self):
		return self
	def __next__(self):
		if self.current > self.high:
			raise StopIteration
		else:
			self.current += 1
			return self.current - 1
c = Mycounter(1,10)
for i in c:
	print(i, end=' ')
"""

# 제너레이터
# 제너레이터(generators)는 키워드 yield를 사용하여서
# 함수로부터 이터레이터를 생성하는 하나의 방법이다.
"""
def myGenerator():
	yield 'first'
	yield 'second'
	yield 'third'
for i in myGenerator():
	print(i)
"""

# 클로저
# 클로저(closure)는 함수에 의하여 반환되는 함수이다.
"""
def addNumber(fixedNum):
	def add(number):
		return fixedNum+number
	return add
func = addNumber(10)
print(func(20))
"""
# Lab: 피보나치 이터레이터
# 피보나치 수열이란 앞의 두 수의 합이 바로 뒤의 수가 되는 수열을 의미한다.
# 피보나치 수열의 수들을 생성하는 이터레이터 클래스를 정의해보자.
# 1 1 2 3 5 8 13 21 34
# FibIterator / a=1, b=0, maxValue=50
"""
class FibIterator:
	def __init__(self,a,b,maxValue):
		self.a = a
		self.b = b
		self.maxValue = maxValue
	def __iter__(self):
		return self
	def __next__(self):
		n = self.a + self.b
		if n > self.maxValue:
			raise StopIteration
		self.a = self.b
		self.b = n
		return n
for i in FibIterator(1,0,50):
	print(i,end=' ')
"""

# 연산자 오버로딩
# 예제
# Impossible + Dream
"""
a = 'Impossible '
b = 'Dream'
c = a.__add__(b)
print(c)
"""
"""
class Point:
	def __init__(self,x=0,y=0):
		self.x = x
		self.y = y
p1 = Point(1,2)
p2 = Point(3,4)
print(p1+p2)
# 오류!
"""
"""
class point:
	def __init__(self,x=0,y=0):
		self.x = x
		self.y = y
	def __add__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		return point(x,y)
	def __str__(self):
		return 'point('+str(self.x)+','+str(self.y)+')'
p1=point(1,2)
p2=point(3,4)
print(p1+p2)
"""

# Lab: 피보나치 이터레이터
# 책을 나타내는 Book 클래스를 작성하고 Book 클래스 내부에
# __add__() 함수를 정의하여서
# Book 클래스의 객체들을 서로 합할 수 있게 하라.
# __add__() 함수는 책의 페이지들을 합쳐서 반환한다.
# >>> book1 = Book('자료구조', 600)
# >>> book2 = Book('C언어', 700)
# >>> book1+book2
# 1300
"""
class Book:
	title=''
	pages=0
	def __init__(self,title='',pages=0):
		self.title=title
		self.pages=pages
	def __str__(self):
		return self.title
	def __add__(self, other):
		return self.pages + other
"""

# 모듈
# 파이썬에서 모듈(module)이란 함수나 변수 또는 클래스 들을 모아 놓은 파일이다.
"""
def fib(n):
	a,b=0,1
	while b<n:
		print(b,end='')
		a,b=a,a+b
	print()
def fib2(n):
	a,b=0,1
	result = []
	while b<n:
		print(b,end='')
		result.append(b)
		a,b=b,a+b
	return result
"""

# 모듈 실행하기
"""
if __name__ == '__main__':
	import sys
	fib(int(sys.argv[1]))
"""

# copy 모듈
# ["red", "blue", "green"]
"""
import copy
colors = ["red", "blue", "green"]
clone = copy.deepcopy(colors)

clone[0] = 'white'
print(colors)
print(clone)
"""

# keyword 모듈
# 변수 이름을 입력하시오: for
# for 은 예약어임.
# 아래는 키워드의 전체 리스트임:
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class',
# 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for',
# 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
# 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
#	  ("변수 이름을 입력하시오: ")
#     print (name, "은 예약어임.")
#     print ("아래는 키워드의 전체 리스트임: ")
#	  "은 사용할 수 있는 변수이름임."
"""
import keyword

name = input("변수 이름을 입력하시오: ")

if keyword.iskeyword(name):
	print(name,"은 예약어임.")
	print("아래는 키워드의 전체 리스트임: ")
	print(keyword.kwlist)
else:
	print(name,"은 사용할 수 있는 변수이름임.")
"""

# random 모듈
# 1~6중 랜덤으로 숫자 2개 뽑기
# 랜덤 수 * 100
# myList = [ "red", "green", "blue" ]
# 랜덤초이스로 아무거나 뽑기
"""
import random
print(random.randint(1,6))
print(random.randint(1,6))
print(random.random()*100)
myList = [ "red", "green", "blue" ]
print(random.choice(myList))
"""

# random 모듈
# 셔플 예제
# 0 ~ 101까지 중 3의 배수 아무거나 3번 뽑기
"""
import random

myList = [[x] for x in range(10)]
random.shuffle(myList)
print(myList)

for i in range(3):
	print(random.randrange(1,101,3))
"""

# os 모듈
"""
import os
os.system('calc')

print(os.getcwd())
print(os.chdir("D:\\tmp"))
print(os.getcwd())

print(os.listdir("."))
"""

# sys 모듈
# 현재 py 파일 경로 (prefix)
# 파이썬이 설치된 경로 (executable)
# executable
"""
import sys
print(sys.prefix)
print(sys.executable)
"""

# time 모듈
"""
import time
print(time.time())
"""

# time 피보나치 예제
""""
import time
def fib(n):
	a,b=0,1
	while b<n:
		print(b,end='')
		a,b=b,a+b
	print()
start = time.time()
fib(1000)
end = time.time()
print(end-start)
"""

# calender 모듈
"""
import calender

cal = calender(2016,8)
print(cal)
"""

# Lab: 동전 던기지 게임
# 하나의 예제로 동전 던지기 게임을 파이썬으로 작성해보자. random 모듈을 사용한다.
# 동전 던지기를 계속하시겠습니까?( yes, no) yes
# head
# 동전 던지기를 계속하시겠습니까?( yes, no) yes
# head
# 동전 던지기를 계속하시겠습니까?( yes, no) yes
# tail
# 동전 던지기를 계속하시겠습니까?( yes, no) yes
# tail
# 동전 던지기를 계속하시겠습니까?( yes, no) yes
# head
# 동전 던지기를 계속하시겠습니까?( yes, no) no
"""
import random
myList = ['head','tail']

while True:
    response = input("동전던지기를 계속하시겠습니까?( yes, no)")
    if response == 'yes':
        print(random.choice(myList))
    else:
        break
"""