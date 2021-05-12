def prime(number):
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

    if number < 1:
        raise ValueError('ERROR')

    nth_prime = 1
    c = 2
    while nth_prime < number:
        c += 1
        if is_prime(c) == True:
            nth_prime += 1

    return c
