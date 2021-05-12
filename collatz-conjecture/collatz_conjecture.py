def steps(number):
    if number < 1:
        raise ValueError("Bad input")
    count_steps = 0
    while number != 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = number * 3 + 1
        count_steps += 1
    return count_steps
