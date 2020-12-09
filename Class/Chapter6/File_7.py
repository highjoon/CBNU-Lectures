f = open("C:\\Pythonsource\\Class\\CBNU_Advanced_Business_Programming\\Class\\Chapter6\\README.txt")
lines = f.readlines()
line_no = 0
f.close()
count = 0
for line in lines:
    line_no += 1
    if "Python" in line:
        count = count + 1
        print(line_no, ":" + line)
print("no_of_lines=", count)
