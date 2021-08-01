# Lab: 함수의 튜플 반환 예제
# 원의 넓이와 둘레를 동시에 반환하는 함수를 작성, 테스트해보자.
"""
import math

def calCircle(r):       # 반지름이 r인 원의 넓이와 둘레를 동시에 반환하는 함수  (area, circum)
    area  = math.pi * r * r
    circum = 2 * math.pi * r
    return (area, circum)

radius = float(input("원의 반지름을 입력하시오: "))
(a, c) = calCircle(radius)
print("원의 넓이는 "+str(a)+"이고 원의 둘레는"+str(c)+"이다.")
"""
"""
numbers = {2,1,3}
print(numbers)  # 정렬되서 프린트됨.

for x in numbers:
    print(x,end='')

print()
# 튜플에서는 인덱싱이 불가능. numbers[0] 이런거 안됨!

numbers.add(4)
print(numbers)
"""
"""
A = {1,2,3,4,5}
B = {1,2,3}

print(B<A)
print(B.issubset(A))    # b가 a의 부분집합이냐?
"""

# 집합 연산 # 외울것
"""
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)
# {1, 2, 3, 4, 5}


print(A & B)
# {3}

print(A - B)
# {1, 2}
"""

# Lab: 파티 동시 참석자 알아내기
# 파티에 참석한 사람들의 명단이 세트 A와 B에 각각 저장되어 있다.
# 2개 파티에 모두 참석한 사람들의 명단을 출력하려면 어떻게 해야 할까?
# 2개의 파티에 모두 참석한 사람은 다음과 같습니다.
# {'Park'}
"""
partyA = set(["Park", "Kim", "Lee"]) # 중괄호의 역할
partyB = set(["Park", "Choi"])       # 중괄호의 역할

print("2개의 파티에 모두 참석한 사람은 다음과 같습니다. ")
print ( partyA.intersection(partyB))
"""

# Lab: 파일에서 중복되지 않은 단어의 개수
# 텍스트 파일을 읽어서 단어를 얼마나 다양하게 사용하여 문서를 작성하였는지를 계산하는 프로그램을 작성해보자.
# 입력 파일 이름: proverbs.txt
# 사용된 단어의 개수= 18
# {'travels', 'half', 'that', 'news', 'alls', 'well',
# 'fast', 'feather', 'flock', 'bad', 'together',
# 'ends', 'is', 'a', 'done', 'begun', 'birds', 'of'}

# 단어에서 구두점을 제거하고 소문자로 만든다.
"""
def process(w):
    output =""
    for ch in w:
        if( ch.isalpha() ):
            output += ch
    return output.lower()
words = set()

# 파일을 연다.
fname = input("입력 파일 이름: ")
file = open(fname, "r")     # fname의 파일을 읽기형식 (reading)으로 불러온다.

# 파일의 모든 줄에 대하여 반복한다.
for line in file:   # 1줄씩 갖고온다.
    lineWords = line.split()    # 갖고온 줄을 각 단어로 분할함.
    for word in lineWords:
        words.add(process(word))	# 단어를 세트에 추가한다.

print("사용된 단어의 개수=", len(words))
print(words)
"""

"""
# split 함수
a = "Life is too short"
# a = ['Life', 'is', 'too', 'short']
b = "a:b:c:d"
# b.split(':')
# ['a', 'b', 'c', 'd']
"""

# 항목 접근하기
"""
contacts = {'Kim':'01012345678',  'Park':'01012345679', 'Lee':'01012345680' }
print(contacts['Kim'])
print(contacts.get('Kim'))

contacts['Choi'] = '01056781234'
print(contacts)

contacts.pop("Kim")
print(contacts)
"""

# Lab: 영한 사전 만들기
# 우리는 영한 사전을 구현하여 보자.
# 어떻게 하면 좋은가?
# 공백 딕셔너리를 생성하고 여기에 영어 단어를 키로 하고
# 설명을 값으로 하여 저장하면 될 것이다.
# 단어를 입력하시오: one
# 하나
# 단어를 입력하시오: python
# 없음
"""
english_dict = dict()

english_dict['one'] = '하나'
english_dict['two'] = '둘'
english_dict['three'] = '셋'

word = input("단어를 입력하시오: ")
print (english_dict.get(word, "없음"))
"""

# Lab: 단어 카운터
# 사용자가 지정하는 파일을 읽어서 파일에 저장된
# 각각의 단어가 몇 번이나 나오는지를 계산하는 프로그램을 작성하여 보자.
"""
fname = input("파일 이름: ")
file = open(fname, "r")

table = dict()
for line in file:
    words = line.split()
    for word in words:
        if word not in table:
            table[word] = 1
        else:
            table[word] += 1

print(table)
"""

# Lab: 축약어 풀어쓰기
# 현대인들은 축약어를 많이 사용한다.
# 예를 들어서 "B4(Before)" "TX(Thanks)" "BBL(Be Back Later)"
# "BCNU(Be Seeing You)" "HAND(Have A Nice Day)"와 같은 축약어들이 있다.
# 축약어를 풀어서 일반적인 문장으로 변환하는 프로그램을 작성하여 보자.
# 번역할 문장을 입력하시오: TX Mr. Park!
# Thanks Mr.Park!
"""
table = { "B4": "Before",
          "TX": "Thanks",
          "BBL": "Be Back Later",
          "BCNU":"Be Seeing You",
          "HAND":"Have A Nice Day" }

message = input('번역할 문장을 입력하시오: ')
words = message.split()
result = ""
for word in words:
    if word in table:
        result += table[word] + " "
    else:
        result += word

print(result)
"""

# 문자열 비교하기
# 문자열을 입력하시오: apple
# 문자열을 입력하시오: orange
# apple 가 앞에 있음
# 알파벳 순서를 기준으로!
"""
a = input("문자열을 입력하시오: ")
b = input("문자열을 입력하시오: ")
if( a < b ):
	print(a, "가 앞에 있음")
else:
	print(b, "가 앞에 있음")
"""

# 문자열에서 단어 분리
"""
s = 'Never put off till tomorrow what you can do today.'
print(s.split())
# ['Never', 'put', 'off', 'till', 'tomorrow', 'what', 'you', 'can', 'do', 'today.']
"""

# Lab: 회문 검사하기
# 회문(palindrome)은 앞으로 읽으나 뒤로 읽으나 동일한 문장이다.
# 예를 들어서 "mom", "civic", "dad" 등이 회문의 예이다.
# 사용자로부터 문자열을 입력받고 회문인지를 검사하는 프로그램을 작성하여 보자.
# 문자열을 입력하시오: dad
# 회문입니다.
"""
def check_pal(s):
    low = 0
    high = len(s) - 1

    while True:
        if low > high:
            return True;

        a = s[low]
        b = s[high]

        if a != b:
            return False
        low += 1
        high -= 1

s = input("문자열을 입력하시오: ")
s = s.replace(" ", "")

if( check_pal(s)==True):
            print("회문입니다.")
else:
            print("회문이 아닙니다.")

"""

# Lab: 머리 글자어 만들기
# 머리 글자어(acronym)은 NATO(North Atlantic Treaty Organization)처럼
# 각 단어의 첫글자를 모아서 만든 문자열이다.
# 사용자가 문장을 입력하면 해당되는 머리 글자어를 출력하는 프로그램을 작성하여 보자.
# 문자열을 입력하시오: North Atlantic Treaty Organization
# NATO
"""
phrase  = input("문자열을 입력하시오: ")
  
acronym = ""
for word in phrase.upper().split():
	acronym += word[0]
  
print( acronym )

"""

# Lab: CSV 파일 분석
# CSV 파일은 split() 메소드를 이용하여 파싱될 수 있다.
# open(), readlines(), strip() 메소드를 사용하여서
# 다음과 같은 CSV 파일에서 데이터를 읽는 프로그램을 작성하여 보자.
# 홍길동,2018,생활관A,312,3.18
# 홍길동
# 2018
# 생활관A
# 312
# 3.18
# 김철수,2017,생활관B,102,3.25
# 김철수
# 2017
# 생활관B
# 102
# 3.25
# …
"""
# 파일을 오픈한다.

f = open("E:\\students.txt", "r")

# 파일의 각 줄에 대하여 반복한다. 
for line in f.readlines():

    # 공백 문자를 제거한다. 
    line = line.strip()

    # 줄을 출력한다.
    print(line)

    # 줄을 단어로 분리한다. 
    words = line.split(",")

    # 줄의 단어를 출력한다.
    for word in words:
        print("   ", word)
"""

# Lab: 문자열 분석
# 문자열 안에 있는 문자의 개수, 숫자의 개수, 공백의 개수를 계산하는 프로그램을 작성하여 보자.
# 문자열을 입력하시오: A picture is worth a thousand words.
# {'digits': 0, 'spaces': 6, 'alphas': 29}
"""
sentence = input("문자열을 입력하시오: ")

table = { "alphas": 0, "digits":0, "spaces": 0 }

for i in sentence:
   if i.isalpha():
      table["alphas"] += 1
   if i.isdigit():
      table["digits"] += 1
   if i.isspace():
      table["spaces"] += 1

print(table)
"""

# strip은 공백을 없애주는 함수
# s = [' 홍길동 ']
# ss = s.strip()
# print(ss)     # ['홍길동'] 으로 출력됨.