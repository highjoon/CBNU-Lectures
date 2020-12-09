class myClass:
    def __init__(self, value):
        self.value  = value
        print("Class is created, value = ", value)

    def __del__(self):
        print("Class is deleted")

def foo():
    myClass(200)

foo()