infile = open("C:\\Pythonsource\\Class\\CBNU_Advanced_Business_Programming\\Class\\Chapter6\\news.txt", "r", encoding='UTF8')

for line in infile:
    line = line.rstrip()
    # 파이썬 rstrip ()은 문자열의 지정된 문자열의 끝을 (기본값은 공백입니다) 삭제합니다.
    word_list = line.split()
    # split 함수는 a.split()처럼 괄호 안에 아무 값도 넣어 주지 않으면 공백(스페이스, 탭, 엔터 등)을 기준으로 문자열을 나누어 준다.
    for word in word_list:
        print(word)

infile.close()