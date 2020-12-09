class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print("My name is {0} and age is {1}".format(self.name, self.age))

class Student(Person):
    def __init__(self, name, age, id , dept):
        self.name = name
        self.age = age
        self.id = id
        self.dept = dept
    def intro(self):
        print("My name = {0} and age = {1}, and id={2}, dept={3}".format(self.name, self.age, self.id, self.dept))

p1 = Person("Cho", 22)
p1.intro()
p2 = Person("Park", 24)
p2.intro()
s1 = Student("Kim", 25, 100, "MIS")
s1.intro()