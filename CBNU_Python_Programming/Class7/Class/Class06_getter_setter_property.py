class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = 0
        self.set_age(age)

    def get_age(self):  # getter
        return self.__age

    def set_age(self, age):  # setter
        if 0 < age < 150:
            self.__age = age


p = Person('홍길동', -30)
print(p.name, p.get_age())
p.set_age(30)
print(p.name, p.get_age())
