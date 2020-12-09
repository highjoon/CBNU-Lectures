infile = open("C:\\Pythonsource\\Class\\CBNU_Advanced_Business_Programming\\Class\\Chapter6\\sales.txt", 'r')
sum = 0
line = infile.readlines()
line = list(map(float, line))
num = len(line)
# map은 리스트의 요소를 지정된 함수로 처리해주는 함수.

for i in line:
    sum += i

avg = sum / num

print("-------- 매출 보고서 --------")
print("총 매출 =", int(sum))
print("평균 일매출 =", avg)