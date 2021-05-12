from fractions import Fraction

def triplets_with_sum(n):
    triplets_found = []
    for a in range(1, int(n/3)):
        b = Fraction(n**2//2 - n*a, n-a)
        if b.denominator != 1: continue
        c = n - a - b
        if a < b < c:
            triplets_found.append([a, int(b), int(c)])
    return triplets_found

