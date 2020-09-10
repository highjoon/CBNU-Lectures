"""
# 변수

num = int(input("참석자의 수를 입력하시오 : "))
chickens = num * 1
beers = num * 2
cakes = num * 4
print("치킨의 수 :",chickens)
print("맥주의 수 :",beers)
print("케익의 수 :",cakes)
"""
"""
# 변수 값 교환

x = 20
y = 10

x = y
print(x)# x = 10
y = x   
print(y)# y = 10

z = x
y = z # y = 20
print(y)
"""

"""
# 이 프로그램은 사용자로부터 2개의 정수를 받아서 합을 계산한다.

x = int(input("첫 번째 정수 :"))
y = int(input("두 번째 정수 :"))
sum = x + y
print("합은",sum)
diff = x - y
print("차는",diff)
"""

# 예제

mymoney = 5000
candyprice = 120
# 최대한 살 수 있는 사탕 수
numcandies = mymoney//candyprice
# 최대한 사탕을 구입하고 남은 돈
change = mymoney%candyprice
print("최대한 살 수 있는 사탕 수 : ",numcandies,"개",sep="")
print("최대한 사탕을 구입하고 남은 돈 : ",change,"원",sep="")
"""
"""
weekpotatoes = 20 + (-10 + 40) * 52
print("1년 동안 수확하는 감자 갯수 :",weekpotatoes,"개")
yeareatpotatoes = 3 * 365
print("1년 동안 먹는 감자 갯수 :",yeareatpotatoes,"개")
yearpotatoes = weekpotatoes - yeareatpotatoes
print("1년 후의 감자 갯수 :",yearpotatoes,"개")

"""
# 복리 계산
init_money = 24
interest = 0.06
years = 382

principal_money = init_money*(1+interest)**years
print(principal_money)
"""
"""
# 등산 시속 계산
from math import *
flatland1 = 10/20
height = sqrt(3**2+4**2)
uphill = height/10
downhill = height/30
flatland2 = 8/20
total_time = flatland1 + uphill + downhill + flatland2
print(total_time)
"""
"""
# 구의 부피 계산하기
r = 5.0
volume = (4.0/3.0) * 3.141592 * r**3
print(volume)
"""
"""
# 구의 부피 계산하기2
distance = 40 * 10**12
light_speed = 300000    # 빛의 속도 = 300000
secs = distance / light_speed   # 별 까지 가는 시간
light_year = secs/(60.0*60.0*24.0*365.0)    # 별 까지 가는 광년
print(light_year)
"""
"""
# 대화하는 프로그램 만들기 1
user_name = input("사용자의 이름을 입력하세요. :")
user_age = int(input("사용자의 나이를 입력하세요. :"))
user_age_10years_later = user_age + 10
print(user_name,"님 반갑습니다!",sep = "")
print("10년 후면 ",user_age_10years_later,"살이 되시는군요!",sep = "")
"""

# 대화하는 프로그램 만들기 2 (자동판매기)
price = int(input("물건값을 입력하시오. :"))
note = int(input("1000원 지폐 갯수 :"))
coin500 = int(input("500원 동전 갯수 :"))
coin100 = int(input("100원 동전 갯수 :"))
change = (note * 1000) + (coin500 * 500) + (coin100 * 100) - price

ncoin500 = change//500
change = change%500

ncoin100 = change//100
change = change%100

ncoin10 = change//10
change = change%10

ncoin1 = change//1
change = change%1

print("500원 =",ncoin500,"100원 =",ncoin100,"10원 =",ncoin10,"1원 =",ncoin1)

"""
# 특수 문자열

# 문자 앞에 \가 붙으면 문자의 특수한 의미를 잃어버린다.

message = 'doesn\'t'
print(message)

message2 = "\"yes,\"he said"
print(message2)
"""
"""
# 문자열의 출력
price = 10000
print("상품의 가격은 %s원 입니다."%price)
"""
"""
# 숫자 추측 게임 (인덱싱 사용)
first = input("첫 번째 단어를 입력해주세요. :")
second = input("두 번째 단어를 입력해주세요. :")
third = input("세 번째 단어를 입력해주세요. :")
acronym = first[0]+second[0]+third[0]
print(acronym)
"""
# 리스트
"""
shopping_list = ['milk', 'water', 'foods']
print(shopping_list)
"""