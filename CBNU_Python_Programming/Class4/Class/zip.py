names = ['홍길동', '임꺽정', '유관순']
ages = [19, 30, 25, 100]
genders = ['남', '남', '여']
for name, age, gender in zip(names, ages, genders):
    print('이름:', name, '나이:', age, '성별:', gender)
