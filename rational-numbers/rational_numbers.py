from __future__ import division
from math import gcd


class Rational:
    def __init__(self, numer, denom):
        self.numer, self.denom = self.pretty(numer, denom)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        a1, b1, a2, b2 = self.helper(other)
        return Rational((a1 * b2 + a2 * b1), (b1 * b2))

    def __sub__(self, other):
        a1, b1, a2, b2 = self.helper(other)
        return Rational((a1 * b2 - a2 * b1), (b1 * b2))

    def __mul__(self, other):
        a1, b1, a2, b2 = self.helper(other)
        return Rational((a1 * a2), (b1 * b2))

    def __truediv__(self, other):
        a1, b1, a2, b2 = self.helper(other)
        return Rational((a1 * b2), (a2 * b1))

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        a, b, _, _ = self.helper()
        return Rational((a**power), (b**power))
        
    def __rpow__(self, base):
        a, b, _, _ = self.helper()
        return (base**a) ** (1/b)

    @staticmethod
    def pretty(numer, denom):
        divisor = gcd(numer, denom)
        numer = numer // divisor
        denom = denom // divisor
        if denom < 0:
            numer *= -1
            denom *= -1
        return numer, denom

    def helper(self, other=None):
        a1 = self.numer
        b1 = self.denom
        if other:
            a2 = other.numer
            b2 = other.denom
        else:
            a2, b2 = None, None
        return (a1, b1, a2, b2)

