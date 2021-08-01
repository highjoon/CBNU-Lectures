import re


class TextWording:
    def __init__(self, file, start, end):
        self.file = file
        self.start = start
        self.end = end
        self.characters = ",.[]()-'\""
        self.li = []
        self.count = {}

    @property
    def replaceWord(self):
        for x in range(len(self.characters)):
            self.file = self.file.replace(self.characters[x], " ")
        self.text = self.file.split(" ")
        return self.text

    @property
    def appendWord(self):
        for x in self.replaceWord:
            if re.findall(r'^' + self.start, x) and re.findall('\w+' + self.end, x):
                self.li.append(x)
        return self.li

    @property
    def countWord(self):
        for i in self.appendWord:
            try:
                self.count[i] += 1
            except:
                self.count[i] = 1
        return self.count


with open('text.txt') as fin:
    fi = fin.read().lower()

st_word = str(input("시작 문자열 입력 : "))
en_word = str(input("끝 문자열 입력 : "))

case = TextWording(fi, st_word, en_word)
result = case.countWord

print("\n{0}로(으로) 시작하고 {1}로(으로) 끝나는 단어 목록".format(st_word, en_word))
for key, value in result.items():
    print("{0}: {1}".format(key, value))
