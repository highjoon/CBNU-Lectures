# Lab : 파티 준비
# 참석자에 맞추어서 치킨(1인당 1마리), 맥주(1인당 2캔), 케익(1인당 4개)를 출력하는 프로그램을 작성해보자.
# 참석자의 수를 입력하시오:25, 치킨의 수:  25, 맥주의 수:  50, 맥주의 수:  50
"""
number = int(input("참석자의 수를 입력하시오. :"))
chickens = number * 1
beers = number * 2
cakes = number * 4
print("치킨의 수",chickens)
print("맥주의 수",beers)
print("케익의 수",cakes)
"""

# 변수 값 교환
# 변수 x 와 변수 y의 값을 서로 바꾸는 프로그램을 작성해보자. (x = 10, y = 20)
"""
x = 10
y = 20

z = x
x = y
y = z

print("x =",x,"y =",y)
"""

# 낙타체는 변수의 첫 글자는 소문자로, 나머지 단어 의 첫 글자는 대문자로 적는 방법이다.
# 예를 들면, myNewCar처럼 첫 'm'은 소문자로, 나머지 단어들의 첫 글 자는 대문자로 표기한다


# 이 프로그램은 사용자로부터 2개의 정수를 받아서 합을 계산한다.
# x = 첫 번째 정수, y = 두 번째 정수, 합 구하기, 차 구하기
"""
x = int(input("첫 번째 정수 :"))
y = int(input("두 번째 정수 :"))

sum = x + y
diff = x - y

print("합은",x + y)
print("차는",x - y)
"""

# 예제
# 하나의 예로 현재 5000원이 있고 사탕의 가격이 120원이라고 하자. 최대한 살 수 있는 사탕의 개수와 나머지 돈은 얼마인가?
"""
mymoney = 5000
candyprice = 120

numcandies = mymoney // candyprice
change = mymoney % candyprice

print("최대한 살 수 있는 사탕의 개수 :",numcandies)
print("나머지 돈 :",change)
"""

# Lab: 감자 재배
# 우주인이 화성이 가서 자급자족하기 위하여 감자를 재배한다고 가정하자.
# 처음에 20개의 감자가 있었고 매주 감자 10개를 심어서 40개를 수확한다고 하자.
# 또 하루에 감자를 3개씩 먹는다고 가정하자. 1년(52주)이 흐르면 감자는 몇 개가 될까?
"""
weekpotatoes = 20 + ((40 - 10) * 52)
daypotatoes = 3 * 365

yearpotatoes = weekpotatoes - daypotatoes

print("1년 후 감자 갯수 :",yearpotatoes)
"""

# 복리 계산
# 1626년에 아메리카 인디언들이 뉴욕의 맨하탄섬을 단돈 60길더(약 24달러)에 탐험가 Peter Minuit에게 팔았다고 한다.
# 382년 정도 경과한 현재 맨하탄 땅값은 약 600억달러라고 한다.
# 하지만 만약 인디언이 24달러를 은행의 정기예금에 입금해두었다면 어떻게 되었을까?
# 예금 금리는 복리로 6%라고 가정하자. 그리고 382년이 지난 후에는 원리금을 계산하여 보자.
# 정기 예금 = init_money, 복리 = interest, 년 = years
# 정기 예금 x ((1 + 복리)^년)
"""
init_money = 24
interest = 0.06
years = 382

total_money = init_money * ((1 + interest)**years)
print("원리금 =",total_money)
"""

# 등산 시속 계산
# 어떤 사람이 산악 자전거로 등산을 계획하고 있다.
# 평지에서는 시속 20km/h가 가능 하고 오르막에서는 10km/h, 내리막에서는 30km/h가 가능하다고 하자.
# 위와 같은 경로를 자전거로 주행한다면 시간이 얼마나 걸릴까?
# math 사용, 평지1 = time1, 오르막 = time2, 내리막 = time3, 평지2 = time4,
# 빗변 = height = 제곱근(밑변 ^ 2 + 높이 ^ 2)
"""
from math import *
time1 = 10 / 20
height = sqrt(3**2 + 4**2)
time2 = height / 10
time3 = height / 30
time4 = 8 / 20

total_time = time1 + time2 + time3 + time4
print("총 소요 시간 :",total_time)
"""

# 구의 부피 계산하기
# 반지름 = r, 부피 = volume = 4.0/3.0 * 3.141592 * r**3
# 반지름 = 5
"""
r = 5
volume = 4.0 / 3.0 * 3.141592 * 5 ** 3
print("구의 부피 :",volume)
"""

# 구의 부피 계산하기2
# 지구에서 가장 가까운 별은 프록시마 켄타우리(Proxima Centauri) 별이라고 한다.
# 프록시마 켄타우리는 지구로부터 40 x 10 ^ 12 km떨어져 있다고 한다.
# 빛의 속도로 프록시마 켄타우리까지 간다면 시간이 얼마나 걸리는지 직접 계산해보기로 하자.
# 거리 = distance, 광속 = light_speed, 초 = secs, 광년 = light_year
# 광속 = 300000, 초 = 거리 / 광속, 광년 = 초 / (60*60*24*365)
"""
distance = 40 * 10**12
light_speed = 300000
secs = distance / light_speed
light_year = secs / (60.0 * 60.0 * 24.0 * 365.0)
print("총 소요 시간 :",light_year)
"""

# 대화하는 프로그램 만들기 1
# 사용자에게 이름을 물어보고 화면에 "철수님 반갑습니다"와 같이 출력한다.
# 이어서 사용 자의 나이를 물어보고 "10년 후면 30살이 되시는군요!"와 같이 출력하도록 파이썬 프로그램을 작성하라.
# 모든 작업은 파이썬 쉘에서 진행한다.
"""
user_name = input("사용자의 이름을 입력하세요. :")
print("{}님 반갑습니다!".format(user_name))
user_age = int(input("사용자의 나이를 입력하세요. :"))
user_age_10years_later = user_age + 10
print("10년 후면 {}살이 되시는군요!".format(user_age_10years_later))
"""

# 대화하는 프로그램 만들기 2 (자동판매기)
# 자동 판매기를 시뮬레이션하는 프로그램을 작성하여 보자.
# 사용자는 1000원짜리 지폐와 500원짜리 동전, 100원짜리 동전을 사용할 수 있다.
# 물건값을 입력하고 1000원권, 500원짜리 동전, 100원짜리 동전의 개수를 입력하면 거스름돈을 계산하여서 동전으로 반환한다.
# 물건값을 입력하시오: 750
# 1000원 지폐개수: 1
# 500원 동전개수: 0
# 100원 동전개수: 0
# 500원= 0 100원= 2 10원= 5 1원= 0
"""
price = int(input("물건값을 입력하시오."))
notes = int(input("1000원 지폐 개수"))
coin500 = int(input("500원 동전 개수"))
coin100 = int(input("100원 동전 개수"))
change = notes*1000 + coin500*500 + coin100*100 - price

nCoin500 = change // 500
change = change % 500

nCoin100 = change // 100
change = change % 100

nCoin10 = change // 10
change = change % 10

nCoin1 = change

print("500원 = ",nCoin500,"100원 = ",nCoin100,"10원 = ",nCoin10,"1원 =",nCoin1)
"""

# 특수 문자열
# 문자 앞에 \가 붙으면 문자의 특수한 의미를 잃어버린다.
# doesn't 출력하기
# "Yes," he said. 출력하기
"""
message1 = 'doesn\'t'
message2 = "\"Yes,\" he said."

print("message1 =",message1, "/", "message2 =",message2)
"""

# 문자열의 출력
# price = 10000, ("상품의 가격은 %s원 입니다."%price) 사용
"""
price = 10000
print("상품의 가격은 %s원 입니다."%price)
"""

# 숫자 추측 게임 (인덱싱 사용)
# 사용자에게 단어 3개를 입력받아서 약자(acronym: 몇 개 단어의 머리글자로 된 말)를 만들어 보자.
# 예를 들어서  ‘OST’도 Original Sound Track의 약자이다.
# 이 예제는 소스파일로 작성하여 실행해보자.
# 첫 번째 단어를 입력해주세요: Original
# 두 번째 단어를 입력해주세요: Sound
# 세 번째 단어를 입력해주세요: Track
# OST
# 합성어 = acronym
"""
first = input("첫 번째 단어를 입력해주세요 :")
second = input("두 번째 단어를 입력해주세요 :")
third = input("세 번째 단어를 입력해주세요 :")
acronym = first[0] + second[0] + third [0]
print(acronym)
"""

# 리스트
# 쇼핑리스트 = milk, eggs, cheese, butter
"""
shopping_list = ["milk", "eggs", "cheese", "butter"]
print(shopping_list)
"""