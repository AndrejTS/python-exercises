def square(number):
    if not 0 < number < 65:
        raise ValueError(' ')
    return 1 << (number - 1)


def total():
    return 18446744073709551615

