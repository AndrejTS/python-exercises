import math

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        a, b, c, d = self.helper(other)
        return a == c and b == d

    def __add__(self, other):
        a, b, c, d = self.helper(other)
        return ComplexNumber((a+c), (b+d))

    def __mul__(self, other):
        a, b, c, d = self.helper(other)
        return ComplexNumber((a*c - b*d), (a*d + b*c))

    def __sub__(self, other):
        a, b, c, d = self.helper(other)
        return ComplexNumber((a-c), (b-d))

    def __truediv__(self, other):
        numer = self * other.conjugate()
        denom = other * other.conjugate()
        real = numer.real / denom.real
        imag = numer.imaginary / denom.real
        return ComplexNumber(real, imag)

    def __abs__(self):
        a, b, _, _ = self.helper()
        return math.sqrt((a*a + b*b))

    def conjugate(self):
        return ComplexNumber(self.real, -1 * self.imaginary)

    def exp(self):
        a, b, _, _ = self.helper()
        real = math.exp(a) * math.cos(b)
        imag = math.exp(a) * math.sin(b)
        return ComplexNumber(real, imag)

    def helper(self, other=None):
        a = self.real
        b = self.imaginary
        if other:
            c = other.real
            d = other.imaginary
        else:
            c, d = None, None
        return (a, b, c, d)
    
