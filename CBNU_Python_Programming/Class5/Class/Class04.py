def print_profile(**kwargs):
    for k, v in kwargs.items():
        print(str(k) + ': ' + str(v))


print_profile(name='홍길동', age=20, gender='남')
profile = {'name': '심청이', 'age': 18, 'gender': '여'}
print_profile(**profile)  # 딕셔너리 spread
