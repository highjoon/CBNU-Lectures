import os.path

infile = open("C:\\Pythonsource\\Class\\CBNU_Advanced_Business_Programming\\Class\\Chapter6\\sales.txt", 'r')
outfile = open("C:\\Pythonsource\\Class\\CBNU_Advanced_Business_Programming\\Class\\Chapter6\\result.txt", 'w')
sum = 0
line = infile.readlines()
line = list(map(float, line))
num = len(line)
# map은 리스트의 요소를 지정된 함수로 처리해주는 함수.

for i in line:
    sum += i

avg = sum / num

outfile.write("-------- 매출 보고서 --------" + '\n')
outfile.write("총 매출 = " + str(int(sum)) + '\n')
outfile.write("평균 일매출 =" + str(avg) + '\n')
infile.close()
outfile.close()