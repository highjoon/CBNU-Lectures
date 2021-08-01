"""
실습 5) 두 개의 수업을 듣는 학생들

두 과목에 대하여 강의를 듣는 학생 이름을 입력 받고, 두 수업을 같이 듣는 학생들을 출력하는 프로그램을 작성하여라.

입출력 예
파이썬 수업을 듣는 학생 입력: 김철수,임꺽정,홍길동,이순신
C언어 수업을 듣는 학생 입력: 전우치,홍길동,이순신,이영희
두 수업을 모두 듣는 학생: {'홍길동', '이순신'}
"""

python = input("파이썬 : ")
python_list = python.split(',')
python_set = set(python_list)

c = input("파이썬 : ")
c_list = c.split(',')
c_set = set(c_list)

# common = python_set & c_set
common = python_set.intersection(c_set)
print(common)