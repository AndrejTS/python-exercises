from string import ascii_lowercase, digits


def encode(plain_text):
    result = ''
    counter = 0
    for char in plain_text.lower():
        if char in ascii_lowercase:
            index = ascii_lowercase.find(char)
            result += ascii_lowercase[-index-1]
        elif char in digits:
            result += char
        else:
            continue
        counter += 1
        if counter % 5 == 0:
            result += ' '
    result = result.rstrip()
    return result


def decode(ciphered_text):
    result = ''
    for char in ciphered_text.lower():
        if char in ascii_lowercase:
            index = ascii_lowercase.find(char)
            result += ascii_lowercase[-index-1]
        elif char in digits:
            result += char
    return result

