"""
다음과 같은 내용의 모듈(module1.py)이 있다고 할 때, 다음 물음에 답하여라.

v = [1, 2, 3, 4]

def func1(a, b):
    return a + b

def func2(a, b):
    return a ** b

import module1 구문으로 module1을 임포트했을 때, module1의 func1(10, 20)을 호출하여 보아라.
"""
import module1

print(module1.func1(10,20))