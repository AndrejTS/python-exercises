import string


def is_valid(isbn):
    res = 0
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False
    multiplier = 10
    for i in isbn:
        if i in string.digits:
            res += int(i) * multiplier
        elif i == 'X' and multiplier == 1:
            res += 10 * multiplier
        else:
            return False
        multiplier -= 1

    return res % 11 == 0
