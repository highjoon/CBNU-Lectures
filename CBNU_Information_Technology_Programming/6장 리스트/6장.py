"""
scores = [32, 56, 64, 72, 12, 37, 98, 77, 59, 69]

scores[0] = 80
scores[1] = scores[0]

print(scores[0], scores[1])

for element in scores:
    print(element,end=', ')

print()
"""

"""
list1 = list()
list2 = list("Hello")
list3 = list(range(0,5))

print(list1)
print(list2)
print(list3)
"""

"""
list1 = [12,'dog',180.14]
list2 = [['seoul',10],['paris',12],['london',50]]
list3 = ["aaa", ["bbb", ["ccc", ["ddd", "eee", 45]]]]

print(list1)
print(list2)
print(list3)
"""

# Lab: 성적 처리 프로그램
# 학생들의 성적을 처리하는 프로그램을 완성시켜보자. 사용자로부터 성적을 입력받아서 리스트에 저장한다.
# 성적의 평균을 구하고 80점 이상 성적을 받은 학생의 숫자를 계산하여 출력해보자.
# 성적을 입력하시요: 10
# 성적을 입력하시요: 20
# 성적을 입력하시요: 60
# 성적을 입력하시요: 70
# 성적을 입력하시요: 80
# 성적 평균은 48.0 입니다.
# 80점 이상 성적을 받은 학생은 1 명입니다.


# Lab: 문자열 처리 프로그램
# 리스트는 문자열도 저장할 수 있다. 강아지를 많이 키우는 사람을 가정하자.
# 강아지들의 이름을 저장하였다가 출력하는 프로그램을 작성해보자.
# 강아지의 이름을 입력하시오(종료시에는 엔터키) 미나
# 강아지의 이름을 입력하시오(종료시에는 엔터키) 초롱이
# 강아지의 이름을 입력하시오(종료시에는 엔터키) 써니
# 강아지의 이름을 입력하시오(종료시에는 엔터키) 팅커벨
# 강아지의 이름을 입력하시오(종료시에는 엔터키)
# 강아지들의 이름:
# 미나, 초롱이, 써니, 팅커벨,
"""
dognames = []
while True:
    names = input("강아지의 이름을 입력하시오(종료시에는 엔터키)")
    if names == '':
        break
    dognames.append(names)

print("강아지들의 이름 :")
for names in dognames:
    print(names,end=', ')
"""

# 예제
"""
text = "Will is power."
print(text[0], text[3], text[-1])

flist = ["apple", "banana", "tomato", "peach", "pear" ]
print(flist[0], flist[3], flist[-1])
"""

# 슬라이싱
"""
squares = [0, 1, 4, 9, 16, 25, 36, 49]
print(squares[3:6]) # 9, 16, 25 까지 출력. 실제로는 [3]부터 [5]까지
"""

# 리스트는 변경가능
"""
squares = [0, 1, 4, 9, 16, 25, 36, 48]
print(squares)
print(7**2)  # 7의 제곱은 49임!
squares[7] = 49
print(squares)
"""

# 리스트의 기초 연산
# 두개의 리스트를 합칠 때는 연결 연산자인 + 연산자를 사용할 수 있다.
"""
marvel_heroes  = [ "스파이더맨", "헐크", "아이언맨" ]
dc_heroes  = [ "슈퍼맨", "배트맨", "원더우먼" ]
heroes =  marvel_heroes + dc_heroes
print(heroes) # ['스파이더맨', '헐크', '아이언맨', '슈퍼맨', '배트맨', '원더우먼']

values = [ 1, 2, 3 ] * 3
print(values) # [1, 2, 3, 1, 2, 3, 1, 2, 3]
"""

# 요소 찾기
# 어떤 요소가 리스트에 있는지 없는 지만 알려면 in 연산자를 사용하면 된다.
"""
heroes  = [ "스파이더맨", "슈퍼맨", "헐크", "아이언맨", "배트맨" ]
if "배트맨" in heroes :
	print("배트맨은 영웅입니다. ")

heroes  = [ "스파이더맨", "슈퍼맨", "헐크", "아이언맨", "배트맨" ]
index = heroes.index("슈퍼맨")	# index는 1이 된다.
print(index)
"""

"""
# 리스트 복사하기

scores = [ 10, 20, 30, 40, 50 ]
values = scores # values 와 scores 는 같다. 따라서 scores의 값이 바껴도 values의 값도 똑같이 바뀐다.
scores[2] = 9
print(values)

print()

# 리스트 깊은 복사

scores = [ 10, 20, 30, 40, 50 ]
values = list(scores)
values[2]=99    # values의 값만 바뀐다.
scores[2]=100   # scores의 값만 바뀐다.
print(scores)
print(values)
"""

# 리스트 함축
"""
list1 = [3, 4, 5]
list2 = [x*2 for x in list1]
print(list2)    # 6,8,10
"""

# Lab: 피타고라스 삼각형
# 피타고라스의 정리를 만족하는 삼각형들을 모두 찾아보자. 삼각형 한 변의 길이는 1부터 30 이하이다.
# [(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25),
# (8, 15, 17), (9, 12, 15), (10, 24, 26), (12, 16, 20),
# (15, 20, 25), (20, 21, 29)]
"""
new_list = [(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2]
print(new_list)

new_list = []
for x in range(1, 30):
    for y in range(x, 30):
        for z in range(y, 30):
            if x**2+y**2==z**2:
                new_list.append((x, y, z))
print(new_list)
"""

# Lab: 연락처 관리 프로그램
# 파이썬을 이용하여 연락처를 관리하는 프로그램을 작성하여 보자.
# 연락처 관리 프로그램은 다음과 같은 메뉴를 가져야 한다.
"""
--------------------
1. 친구 리스트 출력
2. 친구추가
3. 친구삭제
4. 이름변경
9. 종료
메뉴를 선택하시오: 2
이름을 입력하시오: 홍길동
--------------------
1. 친구 리스트 출력
2. 친구추가
3. 친구삭제
4. 이름변경
9. 종료
메뉴를 선택하시오: 1
['홍길동']
--------------------
...

"""
"""
menu = 0
friends = []
while menu != 9:
    print("--------------------")
    print("1. 친구 리스트 출력")
    print("2. 친구추가")
    print("3. 친구삭제")
    print("4. 이름변경")
    print("9. 종료")
    menu = int(input("메뉴를 선택하시오: "))

    if menu == 1:
        print(friends)

    elif menu == 2:
        name = input("이름을 입력하시오:")
        friends.append(name)

    elif menu == 3:
        del_name = input("지우고자 하는 이름을 입력하시오:")
        if del_name in friends:
            friends.remove(del_name)

    elif menu == 4:
        old_name = input("변경하고자 하는 이름을 입력하시오:")
        if old_name in friends:
            index = friends.index(old_name)
            new_name = input("새로운 이름을 입력하시오:")
            friends[index] = new_name
        else:
            print("이름이 발견되지 않았음")
    elif menu == 9:
        print("종료되었습니다.")
        break
"""

# 2차원 리스트
# 2차원 리스트를 생성한다.
"""
s = [
	[ 1, 2, 3, 4, 5 ] ,
	[ 6, 7, 8, 9, 10 ],
	[11, 12, 13, 14, 15 ]
]
print(s)
"""

# 동적으로 2차원 리스트 생성
# 동적으로 2차원 리스트를 생성한다.
"""
rows = 3
cols = 5

s = [ ]
for row in range(rows):
	s += [[0]*cols]

print("s =", s)
"""

# 2차원 리스트 요소 접근
"""
s = [ 
	[ 1, 2, 3, 4, 5 ] ,
	[ 6, 7, 8, 9, 10 ], 
	[11, 12, 13, 14, 15 ] 
]

# 행과 열의 개수를 구한다. 
rows = len(s)   # 3
cols = len(s[0])    # 5

for r in range(rows):
	for c in range(cols):
		print(s[r][c], end=",")
	print()
"""

# Lab: 연락처 관리 프로그램
# 2개의 주사위를 굴리면 다음 표와 같이 36가지의 결과가 나온다. 이것을 6×6 크기의 2차원 리스트로 생성하여 보자.
"""
rows = 6
cols = 6
table = [ ]

# 2차원 리스트를 생성한다. 
for row in range(rows): 
	table += [[0]*cols]

# 2차원 리스트의 각 요소에 rows와 cols 값을 더하여 저장한다. 
for row in range(rows): 
    for col in range(cols): 
        table[row][col] = (row+1+col+1) 

print(table)
"""

# Lab: TIC-TAC-TOE 게임
# 다음과 같이 텍스트 모드에서 컴퓨터와 사람이 Tic-Tac-Toe 게임을 할 수 있는 프로그램을 작성하여 보자.
"""
   |   |   
---|---|---
   |   |   
---|---|---
   |   |   
다음 수의 x좌표를 입력하시오: 0
다음 수의 y좌표를 입력하시오: 0
  X|  O|   
---|---|---
   |   |   
---|---|---
   |   |   
다음 수의 x좌표를 입력하시오: 1
다음 수의 y좌표를 입력하시오: 1
  X|  O|  O
---|---|---
   |  X|   
---|---|---
   |   |   
...
"""
"""
board= [[' ' for x in range (3)] for y in range(3)]
while True:
	# 게임 보드를 그린다.
    for r in range(3):
        print("   " + board[r][0] + "|   " + board[r][1] + "|   "
              + board[r][2])
        if (r != 2):
            print("---|---|---")

# 사용자로부터 좌표를 입력받는다.
    x = int(input("다음 수의 x좌표를 입력하시오: "))
    y = int(input("다음 수의 y좌표를 입력하시오: "))

# 사용자가 입력한 좌표를 검사한다.
    if board[x][y] != ' ':
        print("잘못된 위치입니다. ")
        continue
    else:
        board[x][y] = 'X'

# 컴퓨터가 놓을 위치를 결정한다. 첫 번째로 발견하는 비어있는 칸에 놓는다.
done = False
for i in range(3):
    for j in range(3):
        if board[i][j] == ' ' and not done:
            board[i][j] = 'O'
            done = True
            break
"""