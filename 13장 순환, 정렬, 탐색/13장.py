# 팩토리얼
"""
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
n = int(input("정수:"))
print(n,"!=",factorial(n))
"""


# 피보나치 수열
# 정수를 입력하시오:10
# 10 번째 피보나치 수는   55
"""
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
n = int(input("정수를 입력하시오:"))
print(n,"번째 피보나치 수는",fib(n))
"""

# 반복을 이용한 피보나치
# 정수를 입력하시오:30
# 30 번째 피보나치 수는   832040
"""
fiboList = {0:0, 1:1}
def fibm(n):
    if not n in fiboList:
        fiboList[n] = fibm(n-1) + fibm(n-2)
    return fiboList[n]
n = int(input("정수를 입력하시오:"))
print(n,"번째 피보나치 수는",fibm(n))
"""
# Lab: 에라스토스의 체
# 소수의 배수를 전부 찾아서 소수가 아니라고 표시한다.
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
"""
def eratosthense(n):
    multiples = set()
    for i in range(2,n+1):
        if not i in multiples:
            yield i
            multiples.update(range(i*i,n+1,i))
print(list(eratosthense(100)))
"""
# 디렉토리 크기 계산
# 순환은 디렉토리의 용량을 계산하는데도 사용될 수 있다.
# 예를 들어 다음과 같은 디렉토리 구조에서
# 루트 디렉토리의 용량을 알려면 어떻게 하여야 할까?
# C:\윤상준\2019년 2학년\2학년 2학기\거시경제학원론 (윤재호 교수님)\시험 준비\5장 시험준비.hwp
"""
import os
def calcDirsize(name):
    totalsize = 0
    if os.path.isfile(name):
        totalsize += os.path.getsize(name)
    else:
        filelist = os.listdir(name)
        for subdir in filelist:
            totalsize += calcDirsize(name+'\\'+subdir)
    return totalsize
name = input("디렉토리:")
print(calcDirsize(name))
"""
# 하노이탑
# 한 번에 하나의 원판만 이동할 수 있다.
# 맨 위에 있는 원판만 이동할 수 있다.
# 크기가 작은 원판위에 큰 원판이 쌓일 수 없다.
# 중간의 막대를 임시적으로 이용할 수 있으나 앞의 조건들을 지켜야 한다.

"""
def hanoi_tower(n,org,tmp,to):
    if (n==1):
        print("원판1을",org,"에서",to,"로 옮긴다.")
    else:
        hanoi_tower(n-1,org,to,tmp)
        print("원판을",org,"에서",to,'로 옮긴다.')
        hanoi_tower(n-1,tmp,org,to)
hanoi_tower(4,'A','B','C')
"""
# Lab: 프랙탈 그래픽
# 이번 장에서 학습한 내용을 바탕으로 순환적으로 나무를 그리는 프랙탈(fractal) 프로그램을 작성해보자.

"""
import turtle

def drawTree(branch,t):
    if branch > 5:
        t.forward(branch)
        t.right(20)
        drawTree(branch-15,t)
        t.left(40)
        drawTree(branch-15,t)
        t.right(20)
        t.backward(branch)

def main():
    t = turtle.Turtle()
    window = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.color("green")
    drawTree(100, t)
    window.exitonclick()

main()
"""

# 선택정렬
# alist = [1, 2, 4, 5, 7, 8, 9]
"""
def selectionSort(alist):
    for i in range(len(alist)):
        minPos = getMinPos(alist,i)
        temp = alist[minPos]
        alist[minPos] = alist[i]
        alist[i] = temp

def getMinPos(alist, start):
    minPos = start
    for i in range(start+1, len(alist)):
        if alist[i] < alist[minPos]:
            minPos = i
    return minPos

alist = [1, 2, 4, 5, 7, 8, 9]
selectionSort(alist)
print(alist)
"""

# 순차 탐색
# False
# True
# testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
"""
def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1
    return found

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13))
"""

# 이진 탐색
# myList = [ 2, 6, 11, 13, 18, 20, 22, 27, 29, 30, 34, 38, 41, 42, 45, 47]
"""
def search_binary(list, value):
    low = 0
    high = len(list) - 1
    while low <= high:
        middle = (low + high) // 2
        if list[middle] > value : high = middle - 1
        elif list[middle] < value : low = middle + 1
        else: return middle
    return -1

myList = [ 2, 6, 11, 13, 18, 20, 22, 27, 29, 30, 34, 38, 41, 42, 45, 47]
print("인덱스 =",search_binary(myList,34))
"""