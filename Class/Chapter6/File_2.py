infile = open("C:\\Pythonsource\\Class\\CBNU_Advanced_Business_Programming\\Class\\Chapter6\\phones.txt", "r")
s = infile.read(10)     # 10글자만 읽는다. (띄어쓰기 포함)
print(s) 

s = infile.readline()   # read(10) 이후  글자 포함 한줄 출력
print(s)

s = infile.readline()   # 그 다음 한줄 출력
print(s)

infile.close()