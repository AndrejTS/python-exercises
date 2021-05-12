letters = 'abcdefghijklmnopqrstuvwxyz'


def find_MMI(a):
    for x in range(1, 26):
        if a * x % 26 == 1:
            return x


def encode(plain_text, a, b):
    if find_MMI(a) is None:
        raise ValueError("Error: a and m must be coprime.")
    plain_text = ''.join(plain_text.split()).lower()
    output = ''
    counter = 0
    for char in plain_text:
        try:
            encoded = (a*letters.index(char) + b) % 26
            output += letters[encoded]
            counter += 1
        except ValueError:
            if char in '123456789':
                output += char
                counter += 1
            else:
                continue
        if counter % 5 == 0:
            output += ' '
    return output.rstrip(' ')


def decode(ciphered_text, a, b):
    MMI = find_MMI(a)
    if MMI is None:
        raise ValueError("Error: a and m must be coprime.")
    ciphered_text = ''.join(ciphered_text.split())
    output = ''
    for char in ciphered_text:
        try:
            decoded = MMI * (letters.index(char) - b) % 26
            output += letters[decoded]
        except ValueError:
            if char in '123456789':
                output += char
    return output
    