"""
입력받은 문자열의 모든 문자 사이에 '-' 삽입하여 출력
"""

s = input("문자열 입력 : ")
letters = list(s)
print('-'.join(letters))

names = ['홍길동','전우치']
joined = ','.join(names)
print(joined)