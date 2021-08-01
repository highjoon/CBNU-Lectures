def surround_h1(fn):
    def func(*args, **kwargs):
        return '<h1>' + fn(*args, *kwargs) + '</h1>'
    return func

@surround_h1
def say_hello(name):
    return 'Hello~, ' + name

print(say_hello('홍길동'))
