def choose_user():
    error_message = '잘못된 입력입니다. 1 ~ 3 사이의 숫자로 입력해주세요.\n'
    choices = ['가위', '바위', '보']
    while True:
        for i, v in enumerate(choices):
            print(i + 1, v)
            """
            1 가위
            2 바위
            3 보
            
            여기서 1 2 3 이 enumerate의 역할
            """
        try:
            index = int(input('선택 > ')) - 1
            if 0 <= index < len(choices):
                return choices[index]
            print(error_message)
        except:
            print(error_message)
            continue

if __name__ == '__main__':
    result = choose_user()
    print(result)