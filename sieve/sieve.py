def primes(limit):
    numbers = [i for i in range(limit + 1)]
    numbers[0] = numbers[1] = False
    for i in range(2, int(limit**0.5 + 1)):
        if numbers[i]:
            for k in range(i * i, limit + 1, i):
                numbers[k] = False
                
    return [i for i in numbers if i]

