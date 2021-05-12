def classify(number):
    if number < 1:
        raise ValueError(' ')
    aliquotSum = 0
    for i in range(1, number//2 + 1):
        if number % i == 0:
            aliquotSum += i
    if aliquotSum == number:
        return 'perfect'
    elif aliquotSum > number:
        return 'abundant'
    else:
        return 'deficient'


print(classify(1))