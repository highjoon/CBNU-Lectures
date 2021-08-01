class Complex:
    def __init__(self, real = 0, image = 0):
        self.real = real
        self.image = image

    def __abs__(self):
        return (self.real ** 2 + self.image ** 2) ** 0.5


com1 = Complex(3, 4)
com2 = Complex()
s = int(abs(com1) + abs(com2))
print(s)