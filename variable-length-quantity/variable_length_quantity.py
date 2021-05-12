from math import ceil


def encode(numbers):
    results = []
    for number in numbers:
        number = bin(number)[2:]
        num_bytes = ceil(len(number) / 7)
        chunks = []
        for _ in range(num_bytes):
            chunks.append(number[-7:].rjust(7, '0'))
            number = number[:-7]
        chunks.reverse()
        for i in range(len(chunks)):
            if i == len(chunks) - 1:
                chunks[i] = '0' + chunks[i]
            else:
                chunks[i] = '1' + chunks[i]
        for byte in chunks:
            results.append(int(byte, 2))     
    return results


def decode(bytes_):
    if bytes_[-1] > 127:
        raise ValueError(' ')
    results = []
    byte_numbers = []
    one_byte_number = []
    for byte in bytes_:
        one_byte_number.append(bin(byte)[2:])
        if byte < 128:
            byte_numbers.append(one_byte_number)
            one_byte_number = []
    for number in byte_numbers:
        for i in range(len(number)):
            number[i] = number[i][-7:].rjust(7, '0')
        results.append(int(''.join(number), 2))
    return results


