import os
os.chdir("C:\\Pythonsource\\Class\\CBNU_Advanced_Business_Programming\\Class\\Chapter6")

dic = {}

f = open('readme.txt', 'r')

for line in f:
    line = line.replace('\n', ' ')
    words = line.split()

    for word in words:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1

# print(dic)
print(dic.get('Python'))
for key in dic:
    if dic[key] > 2:
        print('key = ', key, ': ', dic[key])