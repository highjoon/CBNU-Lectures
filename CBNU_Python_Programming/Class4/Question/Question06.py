"""
사용자가 텍스트를 입력했을 때, 각 단어가 몇 번 나타났는지 카운트 하는 프로그램을 작성하여라.

텍스트 입력은 인터넷에서 텍스트를 복사하여 사용

Hint. 단어는 split() 함수를 이용하여 분리

딕셔너리 컴프리헨션을 사용하여 단어 별로 카운팅을 수행
"""

text = str(input("텍스트 : "))
word = text.split()
a = {letter: word.count(letter) for letter in word}

for k, v in a.items():
    print(k, v)
