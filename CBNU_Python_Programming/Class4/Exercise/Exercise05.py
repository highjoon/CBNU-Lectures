"""
break 사용 예제) 사용자로부터 문자열을 입력 받아 이를 대문자로 바꿔 출력하는 프로그램을 작성하되, q가 입력될 때까지 반복해서 실행하라.
"""
while True:
    s = input('입력: ')
    if s == 'q':
        break
    print(s.upper())
