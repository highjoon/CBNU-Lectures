"""
사용자로부터 공백으로 구분된 단어들을 입력 받아 중복된 단어를
제외한 단어의 수를 출력하는 코드를 작성하시오.
"""

words = input("여러 단어 입력 (공백으로 구분) : ")
word_list = words.split()
word_set = set(word_list)
print(len(word_set))