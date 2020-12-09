infile = open("C:\\Pythonsource\\Class\\CBNU_Advanced_Business_Programming\\Class\\Chapter6\\news.txt", "r", encoding='UTF8')
outfile = open("C:\\Pythonsource\\Class\\CBNU_Advanced_Business_Programming\\Class\\Chapter6\\news_word", "w", encoding='UTF8')

for line in infile:
    line = line.rstrip()
    word_list = line.split()
    for word in word_list:
        outfile.write(word)
        outfile.write("\n")

infile.close()
outfile.close()