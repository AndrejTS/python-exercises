import itertools


def maximum_value(maximum_weight, items):
    all_possibilities = []
    for i in range(1, len(items) + 1):
        possibilities = itertools.combinations(items, i)
        for possibility in possibilities:
            all_possibilities.append(possibility)

    best = 0
    for possibility in all_possibilities:
        weight = 0
        value = 0
        for i in possibility:
            weight += i['weight']
            value += i['value']
        if weight <= maximum_weight and value > best:
            best = value
    return best

########