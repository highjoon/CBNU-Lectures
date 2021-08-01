def calc_total(*args):
    t = 0
    for v in args:
        t += v
    return t


r1 = calc_total(1, 2, 3, 4)
ls = [10, 20, 30, 40]
r2 = calc_total(*ls)  # 리스트 spread
print(r1, r2)
