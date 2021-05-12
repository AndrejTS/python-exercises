def is_prime(m):
    if m <= 1:
        return False
    if m == 2:
        return True
    if m % 2 == 0:
        return False
    d = 3
    max = int(m**0.5)
    while d <= max:
        if m % d == 0:
            return False
        d = d + 2 
    return True


def factors(value):
    factors = []
    while value % 2 == 0:
        factors.append(2)
        value //= 2
    if is_prime(value):
        factors.append(value)
        return factors

    divisor = 3
    while value != 1:
        if value % divisor == 0:
            factors.append(divisor)
            value //= divisor
            while value % divisor == 0:
                factors.append(divisor)
                value //= divisor
            if is_prime(value):
                factors.append(value)
                break
        divisor += 2
    return factors

