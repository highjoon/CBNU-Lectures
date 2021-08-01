"""
딕셔너리의 모든 키 - 값 출력. 오름차순, 내림차순 정렬
"""

d = {'apple': '사과', 'boy': '소년', 'cat': '고양이'}
letters = sorted(d.keys())
rev = sorted(d.keys(), reverse=True)
print(','.join(letters))
print(','.join(rev))