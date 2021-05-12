from itertools import permutations


def right_of(h1, h2):
    return h1 - h2 == 1


def next_to(h1, h2):
    return abs(h1 - h2) == 1


def zebra_puzzle():
    houses = first, _, middle, _, _ = range(5)
    orderings = list(permutations(houses))
    water, zebra, residents = next(
        (WATER, ZEBRA, (Englishman, Spaniard, Ukrainian, Japanese, Norwegian))
        for (red, green, ivory, yellow, blue) in orderings
        if right_of(green, ivory)
        for (Englishman, Spaniard, Ukrainian, Japanese, Norwegian) in orderings
        if Englishman is red
        if Norwegian is first
        if next_to(Norwegian, blue)
        for (coffee, tea, milk, oj, WATER) in orderings
        if coffee is green
        if Ukrainian is tea
        if milk is middle
        for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
        if Kools is yellow
        if LuckyStrike is oj
        if Japanese is Parliaments
        for (dog, snails, fox, horse, ZEBRA) in orderings
        if Spaniard is dog
        if OldGold is snails
        if next_to(Chesterfields, fox)
        if next_to(Kools, horse)
    )
    resident_numbers = dict(
        zip(residents, ['Englishman', 'Spaniard', 'Ukrainian', 
                        'Japanese', 'Norwegian'])
    )
    return [resident_numbers[i] for i in (water, zebra)]


def drinks_water():
    ans, _ = zebra_puzzle()
    return ans


def owns_zebra():
    _, ans = zebra_puzzle()
    return ans
