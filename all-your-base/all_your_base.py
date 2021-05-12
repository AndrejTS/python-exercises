def rebase(input_base, digits, output_base):
    output = []
    if input_base < 2:
        raise ValueError(' ')
    if output_base < 2:
        raise ValueError(' ')
    if any([digit < 0 for digit in digits]):
        raise ValueError(' ')
    if any([digit >= input_base for digit in digits]):
        raise ValueError(' ')
    decimal = to_decimal(input_base, digits)
    while decimal != 0:
        output.insert(0, decimal % output_base)
        decimal //= output_base
    if not output:
        return [0]
    return output


def to_decimal(input_base, digits):
    power = len(digits) - 1
    result = 0
    for digit in digits:
        result += digit * (input_base ** power)
        power -= 1
    return result

