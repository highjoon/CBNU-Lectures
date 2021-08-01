def get_description():
    from random import choice
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possibilities)


if __name__ == '__main__':
    # 이 부분은 이 파일이 메인으로 실행되었을 때만 수행이 됨
    # 테스트 코드를 작성하기 좋음
    w = get_description()
    print(w)