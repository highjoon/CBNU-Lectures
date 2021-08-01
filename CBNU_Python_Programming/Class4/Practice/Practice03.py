"""
실습 3) 단어 카운팅

인터넷으로부터 영문 텍스트를 복사하여 입력 받고, 입력 받은 텍스트의 단어를 카운팅하는 프로그램을 작성하여라.

텍스트 입력: In this example we use two variables, a and b, which are used as part of the if statement to test

결과:
In 1
this 1
example 1
we 3
...

위의 프로그램을 대소문자를 구분하지 않고 카운팅을 하여라.
"""

text = str(input("텍스트 : "))
li = text.split()
a = {letter:text.count(letter) for letter in li}
b = {letter.lower():text.count(letter) for letter in li}

for k, v in a.items():
    print(k, v)

print()

for k, v in b.items():
    print(k, v)