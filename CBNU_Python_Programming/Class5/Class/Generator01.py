def my_range(first, last=None, step=1):
    if last is None:
        last = first
        first = 0
    while first < last:
        yield first
        first += step


ranger = my_range(1, 10)  # ranger는 제너레이터 객체
print(ranger)
for v in ranger:
    print(v)
