from random import choice

def choose_computer():
    return choice(['가위', '바위', '보'])

if __name__ == '__main__':
    for _ in range(10):
        print(choose_computer())