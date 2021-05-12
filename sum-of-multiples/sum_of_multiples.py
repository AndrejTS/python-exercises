def sum_of_multiples(limit, multiples):
    s = {i for k in multiples if k != 0 for i in range(0, limit, k)}
    return sum(s)
