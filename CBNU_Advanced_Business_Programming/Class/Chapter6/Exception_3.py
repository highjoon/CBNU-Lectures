import os
os.chdir("C:\\Pythonsource\\Class\\CBNU_Advanced_Business_Programming\\Class\\Chapter6")
while True:
    try:
        fname = input("파일 이름을 입력하세요 : ")
        infile = open(fname, 'r')
        print("OK, file")
        infile.close()
        break
    except IOError:
        print("파일 " + fname + "을 발견할 수 없습니다. 다시 입력하세요 !")
        continue
print("GoodBye")