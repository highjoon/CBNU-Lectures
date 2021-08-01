class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __get_name(self):
        return self.name

    def get_age(self):
        return self.__age


person = Person('홍길동', 20)
print(person.name)  # OK
print(person.get_age())  # OK
# print(person.__age)  # ERROR
# print(person.__get_name())  # ERROR
print(person._Person__age)  # OK, 맹글링된 __age 속성
