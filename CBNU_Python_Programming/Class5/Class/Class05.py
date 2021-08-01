def f1():
    print('Hello world')


def f2(f):
    f()


a = f1
a()
f2(f1)
