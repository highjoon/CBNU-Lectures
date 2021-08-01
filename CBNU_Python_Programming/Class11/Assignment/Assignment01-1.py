import re

characters = ",.[]()-'\""  # 지워야 할 특수문자들 목록
start = str(input("시작 문자열 입력 : "))
end = str(input("끝 문자열 입력 : "))
li = []  # start로 시작해서 end로 끝나는 단어들을 저장할 리스트
count = {}  # 리스트 li의 각 단어들의 갯수 {'단어 1' : 갯수, '단어 2' : 갯수 ... }

with open('text.txt') as fin:
    file = fin.read().lower()
    # text.txt 파일을 문자열 형식으로 불러오고 모두 소문자로 변환

for x in range(len(characters)):
    file = file.replace(characters[x], " ")
    # 불러온 파일에서 특수문자들을 모두 띄어쓰기로 변환
    # 예를 들어 decision-maker.[38] 또는 a five-person steering council.[39][40][41] 이런 것들 때문에 검색이 잘 안됨
    # 특수문자를 모두 띄어쓰기로 변환하면
    # decision maker  38, a five person steering council  39 40 41 이런식으로 바뀌기 때문에 모든 단어 검색 가능

text = file.split(" ")
# 특수문자들까지 모두 띄어쓰기로 변환했으니까 이제 text.txt 파일을 띄어쓰기를 기준으로 모두 구분함
# ['python', 'was', 'conceived' ... ] 식으로 구분됨 (리스트 형식)

for i in text:
    if re.findall(r'^' + start, i) and re.findall('\w+' + end, i):
        li.append(i)
# re 정규표현식을 사용
# 리스트 text의 각 요소 중에서 start로 시작해서 end로 끝나는 단어가 있는지 확인하고
# 있다면 리스트 li에 저장함

for i in li:
    try:
        count[i] += 1
    except:
        count[i] = 1
# 리스트 li의 각 요소들의 갯수를 파악하여 딕셔너리 count에 저장
# 리스트 li를 반복문으로 돌려서, 단어를 처음 발견했다면 count에 1로 저장.  ->  {'처음 발견한 단어' : 1}
# 이미 발견했던 단어라면 count에서 해당 단어를 찾아서 +1  ->  {'이미 있는 단어' : 2}

print("\n{0}로(으로) 시작하고 {1}로(으로) 끝나는 단어 목록".format(start, end))
for key, value in count.items():
    print("{0}: {1}".format(key, value))
# 출력
