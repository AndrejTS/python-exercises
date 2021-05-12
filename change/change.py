from itertools import combinations_with_replacement


def find_fewest_coins(coins, target):
    if target == 0:
        return []

    for i in range(1, (target // min(coins)) + 1):
        comb = combinations_with_replacement(coins, i)
        for c in comb:
            if sum(c) == target:
                return list(c)

    raise ValueError(' ')



# print(find_fewest_coins([5, 10], 94))

