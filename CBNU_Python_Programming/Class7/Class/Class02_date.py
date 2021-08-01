import time


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def now():  # self 매개변수가 없음
        t = time.localtime()
        return Date(t.tm_year, t.tm_mon, t.tm_mday)

    @staticmethod
    def tomorrow():  # self 매개변수가 없음
        t = time.localtime(time.time() + 86400)  # 하루는 86400초
        return Date(t.tm_year, t.tm_mon, t.tm_mday)


a = Date(1967, 4, 9)
b = Date.now()
c = Date.tomorrow()

print(a.year, a.month, a.day)
print(b.year, b.month, b.day)
print(c.year, c.month, c.day)