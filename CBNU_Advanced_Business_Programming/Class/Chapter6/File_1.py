infile = open("C:\\Pythonsource\\Class\\CBNU_Advanced_Business_Programming\\Class\\Chapter6\\phones.txt", "r")
line = infile.readline()
while line != "":
    print(line)
    line = infile.readline()
infile.close()