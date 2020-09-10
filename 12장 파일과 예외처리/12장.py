# 예제

"""
infile = open("phones.txt", "r")
s = infile.read(10)
print(s);
infile.close()
"""
"""
infile = open("phones.txt","r")
s = infile.readline()
print(s)
s = infile.readline()
print(s)
s = infile.readline()
print(s)
infile.close()
"""
"""
infile = open('C:\\phones.txt','r')
line = infile.readline()
while line != '':
    print(line)
    line = infile.readline()
infile.close()
"""
"""
infile = open("C:\\phones.txt","r")
for line in infile:
    line = line.strip()
    print(line)
infile.close()
"""

# 파일에 데이터 쓰기
# outfile.write("홍길동 010-1234-5678")
# outfile.write("김철수 010-1234-5679")
# outfile.write("김영희 010-1234-5680")
"""
import os.path
outfile = open("C:\\phones.txt","w")
if os.path.isfile("phones.txt"):
    print("동일한 이름의 파일이 존재합니다.")
else:
    outfile.write("홍길동 010-1234-5678")
    outfile.write("김철수 010-1234-5679")
    outfile.write("김영희 010-1234-5680")
outfile.close()
"""

# Lab: 매출 파일 처리
"""
infilename = input("입력파일:")
outfilename = input("출력파일:")
infile = open(infilename,'r')
outfile = open(outfilename,'w')
sum = 0
count = 0
for line in infile:
    dailysale = int(line)
    sum = sum + dailysale
    count += 1
outfile.write("총매출 ="+str(sum)+'\n')
outfile.write("평균매출 ="+str(sum/count))
infile.close()
outfile.close()
"""

# 텍스트 입출력 기법
# 데이터 추가하기
# outfile.write("최무선  010-1111-2222")
# outfile.write("정중부  010-2222-3333")
"""
outfile = open('C:\\phones.txt','a')
outfile.write("최무선  010-1111-2222")
outfile.write("정중부  010-2222-3333")
outfile.close()
"""

# 텍스트 입출력 기법
# 줄바꿈 기호 삭제하기
"""
infile = open('C:\\phones.txt','r')
for line in infile:
    line = line.rstrip()
    print(line)
infile.close()
"""

# 파일에서 단어 읽기
"""
infile = open("C:\\phones.txt","r")
for line in infile:
    line = line.rstrip()
    word_list = line.split()
    for word in word_list:
        print(word)
infile.close()
"""

# 파일 대화 상자
"""
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

readFile = askopenfilename()
if( readFile != None):
    infile = open(readFile, "r")

for line in infile.readlines():
    line = line.strip()
    print(line)

infile.close() 
"""

# Lab: 스페이스 세기
# 텍스트 파일을 열어서 파일 안의 스페이스 문자의 개수와 탭의 개수를 세는 프로그램을 작성하여 보자.
# 파일 이름을 입력하시오: proverbs.txt
# 스페이스 수 = 20, 탬의 수 = 0
"""
def parse_file(path):
    infile = open(path)
    spaces = 0
    tabs = 0
    for line in infile:
        spaces += line.count(' ')
        tabs += line.count('\t')
    infile.close()
    return spaces, tabs

filename = input("파일이름:")
spaces, tabs = parse_file(filename)
print("스페이스 수 = %s, 탭의 수 = %s" % (spaces, tabs))
"""

# Lab: 줄앞에 번호붙이기
# 텍스트 파일을 열어서 각 줄의 앞에 번호를 매겨서 다시 파일에 쓰는 프로그램을 작성해보자.
# infile  = open("proverbs.txt")
# outfile = open("output.txt","w")
# 1: All's well that ends well.
# 2: Bad news travels fast.
# 3: Well begun is half done.
# 4: Birds of a feather flock together.
"""
infile = open("proverbs.txt","r")
outfile = open("output.txt","w")
i = 1
for line in infile:
    outfile.write(str(i)+": "+line)
    i += 1
infile.close()
outfile.close()
"""

# Lab: 각 문자 횟수 세기
# 파일 안의 각 문자들이 몇 번이나 나타나는지를 세는 프로그램을 작성하자.
# {' ': 16, 'e': 12, 'o': 4, 'a': 7, 'u': 1, 'n': 4, 'k': 1, 'A': 1, 'r': 4,
# 'g': 2, 's': 7, 'b': 1, 'd': 4, 'v': 1, 'f': 5, 'w': 3,
# 'B': 2, 'h': 4, 'i': 2, 't': 7, 'l': 11, 'W': 1, '.': 4, "'": 1, 'c': 1}
# C:\\phones.txt
"""
filename = input("파일명:").strip()
infile = open(filename,'r')
freqs = {}
for line in infile:
    for char in line.strip():
        if char in freqs:
            freqs[char] += 1
        else:
            freqs[char] = 1
print(freqs)
infile.close()
"""

# Lab: CSV 파일 읽기
# CSV(Comma Separated Values) 형식은 엑셀과 같은
# 스프레드 쉬트나 데이터베이스에서 가장 널리 사용되는 입출력 형식이다.
# 파이썬은 CSV 형식을 읽기 위해서 csv라고 하는 모듈을 제공한다.
# 이 모듈을 이용하면 CSV 파일을 쉽게 읽을 수 있다.
# 우리는 연습 삼아서 CSV 형식의 파일을 읽는 코드를 작성하여 보자.
# 1/2/2014,5,8,red
#     1/2/2014
#     5
#     8
#     red
# 1/3/2014,5,2,green
#     1/3/2014
#     5
#     2
#     green
# 1/4/2014,9,1,blue
#     1/4/2014
#     9
#     1
#     blue
# strip() -> 공백문자 없애기
# split() -> 단어별로 분리하기
# C:\test.csv
"""
f = open('C:\test.csv','r')
for line in f.readlines():
    line = line.strip()
    print(line)
    parts = line.split(',')
    for part in parts:
        print(' ',part)
"""

# Lab: 파일 암호화
# 예를 들어 평문 “come to me”은
# “FRPH WR PH”으로 바뀐다.
# 시저 암호 방식을 이용하여서
# 파일을 암호화하고 복호화하는 프로그램을 작성하라.
# 원문: the language of truth is simple.
# 암호문: wkh odqjxdjh ri wuxwk lv vlpsoh.
# 복호문: the language of truth is simple.
# key = 'abcdefghijklmnopqrstuvwxyz'
# text = 'The language of truth is simple.'
"""y = 'abcdefghijklmnopqrstuvwxyz'
def encrypt(n, plaintext):
    result = ''
    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l
    return result.lower()
def decrypt(n, ciphertext):
    result = ''
    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l
    return result
n = 3
text = 'The language of truth is simple.'
encrypted = encrypt(n, text)
decrypted = decrypt(n, encrypted)
print('원문:',text)
print('암호문:',encrypted)
print('복호문:',decrypted)
"""

# Lab: 이미지 파일 복사하기.
# 원본 파일 이름을 입력하시오: 123.png
# 복사 파일 이름을 입력하시오: kkk.png
# 123.png를 kkk.png로 복사하였습니다.
# print(filename1+"를 " +filename2+"로 복사하였습니다. ")
"""
filename1 = input('원본')
filename2 = input('복사')
infile = open(filename1, 'rb')
outfile = open(filename2, 'wb')

while True:
    copy_buffer = infile.read(1024)
    if not copy_buffer:
        break
    outfile.write(copy_buffer)
infile.close()
outfile.close()
print(filename1+"를 " +filename2+"로 복사하였습니다. ")
"""

# 임의 접근 파일
# 예제
# 읽은 문자열 :  All's well
# 현재 위치:   10
# 다시 읽은 문자열 :  All's wel
# C:\\phones.txt
"""
infile = open('C:\\phones.txt','r+')
str = infile.read(10)
print('읽은 문자열 :',str)
position = infile.tell()
print('현재 위치 :', position)

postion = infile.seek(0,0)
str = infile.read(10)
print('다시 읽은 문자열 :',str)
infile.close()
"""