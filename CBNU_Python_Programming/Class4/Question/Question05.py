"""
1 ~ 100 사이의 정수를 ', '로 join 하여라.

Hint.
먼저 리스트 컴프리헨션을 사용하여 숫자를 문자열 타입으로 변환해야 하여 join을 해야 한다.
"""
a = [str(x) for x in range(1, 101)]
print(','.join(a))