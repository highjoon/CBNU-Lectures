class DistanceFrom:
    def __init__(self, origin):
        self.origin = origin

    def __call__(self, x):
        return abs(x - self.origin)


distance = DistanceFrom(5)
print(distance(2))  # 결과 : 3
nums = [1, 37, 42, 101, 13, 9, -20]
nums.sort(key=DistanceFrom(10))  # 10에서 가까운 거리로 정렬
print(nums)