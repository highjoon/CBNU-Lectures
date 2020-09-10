# Counter 클래스
"""
class Counter:
    def reset(self):
        self.counter = 0
    def increment(self):
        self.counter += 1
    def get(self):
        return self.counter

a = Counter()

a.reset()
a.increment()
print("카운터 a의 값",a.get())
"""

# 객체 2개 생성하기
"""
a = Counter()
b = Counter()

a.reset()
b.reset()
"""

# 메소드 정의
"""
class Television:
	def __init__(self, channel, volume, on):
		self.channel = channel
		self.volume = volume
		self.on = on

	def show(self):
		print(self.channel, self.volume, self.on)

	def setChannel(self, channel):
		self.channel = channel

	def getChannel(self):
		return self.channel

t = Television(9, 10, True)

t.show()
t.setChannel(11)
t.show()
"""

# 정보 은닉
# 구현의 세부 사항을 클래스 안에 감추는 것
"""
class Student:
	def __init__(self, name=None, age=0):
		self.__name = name
		self.__age = age

obj=Student()
print(obj.__age) # 밖으로 노출되게하고싶지 않으면 언더라인 두개를 써라!
"""

# 접근자와 설정자
# 하나는 인스턴스 변수값을 반환하는 접근자(getters)이고
# 또 하나는 인스턴스 변수값을 설정하는 설정자(setters)이다.
"""
class Student:
	def __init__(self, name=None, age=0):
		self.__name = name
		self.__age = age

	def getAge(self):
		return self.__age

	def getName(self):
		return self.__name

	def setAge(self, age):
		self.__age=age

	def setName(self, name):
		self.__name=name

obj=Student("Hong", 20)
print(obj.getName())
"""

# Lab: 원을 클래스로 표현
# 원을 클래스도 표시해보자.
# 원은 반지름(radius)을 가지고 있다.
# 원의 넓이와 둘레를 계산하는 메소드도 정의해보자.
# 설정자와 접근자 메소드도 작성한다.
"""
import math
class Circle:
	def __init__(self, radius=1.0):
		self.__radius = radius

	def setRadius(self, r):
		self.__radius = r

	def getRadius(self):
		return self.__radius

	def calcArea(self):
		area = math.pi*self.__radius*self.__radius
		return area
	def calcCircum(self):
		circumference = 2.0*math.pi*self.__radius
		return circumference

c1=Circle(10)
print("원의 반지름=", c1.getRadius())
print("원의 넓이=", c1.calcArea())
print("원의 둘레=", c1.calcCircum())
"""

# Lab: 은행 계좌
# 우리는 은행 계좌에 돈을 저금할 수 있고 인출할 수도 있다.
# 은행 계좌를 클래스로 모델링하여 보자.
# 은행 계좌는 현재 잔액(balance)만을 인스턴스 변수로 가진다.
# 생성자와 인출 메소드 withdraw()와 저축 메소드 deposit() 만을 가정하자.
# 통장에서  100 가 출금되었음
# 통장에  10 가 입금되었음
"""
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def withdraw(self, amount):
        self.__balance += amount
        print("통장에 ", amount, "가 출금되었음")
        return self.__balance

    def deposit(self, amount):
        self.__balance -= amount
        print("통장에서 ", amount, "가 입금되었음")
        return self.__balance

a = BankAccount()
a.deposit(100)
a.withdraw(10)
"""

# Lab: 고양이 클래스
# 고양이를 클래스로 정의한다.
# 고양이는 이름(name)과 나이(age)를 속성으로 가진다.
# Missy 3
# Lucky 5

"""
class Cat:
   def __init__(self, name, age):
      self.__name = name
      self.__age = age

   def setName(self, name):
      self.__name = name

   def getName(self):
      return self.__name

   def setAge(self, age):
      self.__age = age

   def getAge(self):
      return self.__age


missy = Cat('Missy', 3)
lucky = Cat('Lucky', 5)

print (missy.getName(), missy.getAge())
print (lucky.getName(), lucky.getAge())
"""

# Lab: 객체 생성과 사용
# 상자를 나타내는 Box 클래스를 작성하여 보자.
# Box 클래스는 가로길이, 세로길이, 높이를 나타내는 인스턴스 변수를 가진다.

"""
class Box:
    def __init__(self, width=0, length=0, height=0):
        self.__width = width
        self.__length = length
        self.__height = height

    def setWidth(self, width):
        self.__width = width;

    def setLength(self, length):
        self.__length = length;

    def setHeight(self, height):
        self.__height = height;

    def getVolume(self):
        return self.__width*self.__length*self.__height

    def __str__(self):
        return '(%d, %d, %d)' % (self.__width, self.__length, self.__height)


box = Box(100, 100, 100)
print(box)
print('상자의 부피는 ', box.getVolume())
"""

# Lab: 자동차 클래스 작성
# 자동차를 나타내는 클래스를 정의하여 보자.
# 예를 들어, 자동차 객체의 경우, 속성은 색상, 현재 속도, 현재 기어 등이다.
# 자동차의 동작은 기아 변속하기, 가속하기, 감속하기 등을 들 수 있다.
# 이 중에서 다음 그림과 같은 속성과 동작만을 추려서 구현해보자.
# (100, 3, white)
"""
class Car:
    def __init__(self, color = 'white', speed = 0, gear = 1):
        self.__color = color
        self.__speed = speed
        self.__gear = gear

    def setSpeed(self, speed):
        self.__speed = speed

    def setGear(self, gear):
        self.__gear = gear

    def setColor(self, color):
        self.__color = color

    def __str__(self):
        return '(%d, %d, %s)' % (self.__speed, self.__gear, self.__color)

mycar = Car()
mycar.setGear(3)
mycar.setSpeed(100)
print(mycar)
"""

# 객체를 함수로 전달할 때
# 우리가 작성한 객체가 전달되면 함수가 객체를 변경할 수 있다.
# 0 	 0
# 1 	 1
# 2 	 4
# 3 	 9
# 4 	 16
# 사각형의 변= 5
# 반복횟수= 5

"""
# 사각형을 클래스로 정의한다. 
class Rectangle:
	def __init__(self, side=0):
		self.side = side

	def getArea(self):
		return self.side*self.side

# 사각형 객체와 반복횟수를 받아서 변을 증가시키면서 면적을 출력한다.
def printAreas(r, n):
	while n >= 1:
		print(r.side, "\t", r.getArea())
		r.side = r.side + 1
		n = n - 1

# printAreas()을 호출하여서 객체의 내용이 변경되는지를 확인한다. 
myRect = Rectangle();
count = 5
printAreas(myRect, count)
print("사각형의 변=", myRect.side)
print("반복횟수=", count)
"""

# 정적 변수
# 이들 변수는 모든 객체를 통틀어서 하나만 생성되고 모든 객체가 이것을 공유하게 된다.
# 이러한 변수를 정적 멤버 또는 클래스 멤버(class member)라고 한다.

# 예제
"""
class Vector2D :
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)

u = Vector2D(0,1)
v = Vector2D(1,0)
w = Vector2D(1,1)
a = u + v
print(a)
"""