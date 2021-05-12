import string


def rows(letter):
    half = make_half(letter)
    return half + half[:-1][::-1]


def make_half(letter):
    rows = string.ascii_uppercase.index(letter) + 1
    width = rows*2 - 1
    result = [[' '] * width for i in range(rows)]
    result[0] = ['A'.center(width)]
    position = width // 2
    for i in range(1, rows):
        cur_letter = string.ascii_uppercase[i]
        result[i][position - 1] = cur_letter
        result[i][position * (-1)] = cur_letter
        position -= 1
    return [''.join(row) for row in result]

