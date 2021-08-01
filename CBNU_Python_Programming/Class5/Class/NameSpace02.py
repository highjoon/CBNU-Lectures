name = '홍길동'

def print_name4():
    global name
    name = '유관순'
    print(name)


print_name4()
print(name)