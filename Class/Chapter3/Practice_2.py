start = int(input("시작 값 : "))
end = int(input("끝 값 : "))
sum = 0

for i in range (start, end+1):
    sum += i

print(sum)