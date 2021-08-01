def my_decorator(fn):
    def func(*args, **kwargs):
        print('Function Name:', fn.__name__)
        print('Positional Arguments:', args)
        print('Keyword Arguments:', kwargs)
        result = fn(*args, **kwargs)
        print('Result:', result)
    return func

def plus(a, b):
    return a + b

print(plus(1, 2))
decorated = my_decorator(plus)
decorated(1, 2)

@my_decorator
def minus(a, b):
    return a-b

# 같은 이름으로 함수를 호출해도 추가된 기능이 적용
minus(1, 2)
