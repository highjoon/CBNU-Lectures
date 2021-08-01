"""
실습 3) 영어 사전 만들기

딕셔너리 타입을 이용하여 사전을 구성하여, 영단어를 입력하면 그 뜻을 출력하는 프로그램을 작성하여라.

단어 입력: apple
뜻: 사과

단어 입력: cat
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
KeyError: 'cat'
"""
dic = {'apple': '사과'}

word = input("단어 입력 : ")