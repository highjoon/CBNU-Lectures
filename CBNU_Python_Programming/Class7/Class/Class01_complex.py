class Complex:
    def __init__(self, real, image):
        self.real = real
        self.image = image

    def add(self, c):
        real = self.real + c.real
        image = self.image + c.image
        return Complex(real, image)

    def sub(self, c):
        real = self.real - c.real
        image = self.image - c.image
        return Complex(real, image)

c1 = Complex(2, 3)
c2 = Complex(4, 5)
c3 = c1.add(c2)
c4 = c1.sub(c2)

print(c1.real, c1.image)
print(c2.real, c2.image)
print(c3.real, c3.image)
print(c4.real, c4.image)