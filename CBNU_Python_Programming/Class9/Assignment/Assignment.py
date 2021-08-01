class Complex:
    def __init__(self, real, image):
        self.real = real
        self.image = image

    def __str__(self):
        op = '+' if self.image >= 0 else '-'
        return '%d %s %di' % (self.real, op, abs(self.image))

    def __neg__(self):
        op = '+' if self.image < 0 else '-'
        return '%d %s %di' % (-self.real, op, abs(self.image))

    def __add__(self, c):
        return Complex(self.real + c.real, self.image + c.image)

    def __sub__(self, c):
        return Complex(self.real - c.real, self.image - c.image)

    def __mul__(self, c):
        return Complex(self.real * c.real, self.image * c.image)

    def __mod__(self, c):
        return Complex(self.real % c.real, self.image % c.image)

    def __floordiv__(self, c):
        return Complex(self.real // c.real, self.image // c.image)

    def __pow__(self, c):
        return Complex(self.real ** c.real, self.image ** c.image)

    def __lshift__(self, c):
        return Complex(self.real << c.real, self.image << c.image)

    def __rshift__(self, c):
        return Complex(self.real >> c.real, self.image >> c.image)

    def __and__(self, c):
        return Complex(self.real & c.real, self.image & c.image)

    def __or__(self, c):
        return Complex(self.real | c.real, self.image | c.image)

    def __xor__(self, c):
        return Complex(self.real ^ c.real, self.image ^ c.image)


c1 = Complex(5, 2)
c2 = Complex(6, 8)
c3 = -c1
c4 = c1 + c2
c5 = c1 - c2
c6 = c1 * c2
c7 = c1 % c2
c8 = c1 // c2
c9 = c1 ** c2
c10 = c1 << c2
c11 = c1 >> c2
c12 = c1 & c2
c13 = c1 | c2
c14 = c1 ^ c2

print("1번 복소수 (__str__) :", c1)
print("2번 복소수 (__str__) :", c2)
print("음화 (__neg__) :", c3)
print("덧셈 (__add__) :", c4)
print("뺄셈 (__sub__) :", c5)
print("곰셈 (__mul__) :", c6)
print("나머지 (__mod__) :", c7)
print("몫 (__floordiv__) :", c8)
print("거듭제곱 (__pow__) :", c9)
print("비트 시프트 (__lshift__) :", c10)
print("비트 시프트 (__rshift__) :", c11)
print("비트 AND 연산 (__and__) :", c12)
print("비트 OR 연산 (__or__) :", c13)
print("비트 XOR 연산 (__xor__) :", c14)