"""
다음 코드들을 실행하여 보아라.

"""
d = {'apple': '사과', 'orange': '오렌지', 'grape': '포도'}
for k in d:  # 또는 for k in d.keys():
    print(k)

print()

for v in d.values():
    print(v)

print()

for item in d.items():
    print(item)

print()

for k, v in d.items():
    print(k, v)
