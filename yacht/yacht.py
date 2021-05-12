from collections import Counter


YACHT = lambda x: 50 if x.count(x[0]) == 5 else 0
ONES = lambda x: x.count(1)
TWOS = lambda x: x.count(2) * 2
THREES = lambda x: x.count(3) * 3
FOURS = lambda x: x.count(4) * 4
FIVES = lambda x: x.count(5) * 5
SIXES = lambda x: x.count(6) * 6
FULL_HOUSE = lambda x: test_full(x)
FOUR_OF_A_KIND = lambda x: test_four(x)
LITTLE_STRAIGHT = lambda x: 30 if test_straight(x) and x[0] == 1 else 0
BIG_STRAIGHT = lambda x: 30 if test_straight(x) and x[0] == 2 else 0
CHOICE = lambda x: sum(x)


def test_straight(dice):
    dice.sort()
    if len(Counter(dice)) == 5:
        if dice[4] == dice[0] + 4:
            return True


def test_full(dice):
    if len(Counter(dice)) == 2: 
        if Counter(dice).most_common(1)[0][1] == 3:
            return sum(dice)
    return 0


def test_four(dice):
    if len(Counter(dice)) in (1, 2):
        if Counter(dice).most_common(1)[0][1] in (4, 5):
            return 4 * Counter(dice).most_common(1)[0][0]
    return 0


def score(dice, category):
    return category(dice)

