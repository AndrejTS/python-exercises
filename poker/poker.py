def best_hands(hands):
    result, max_val = [], None
    for x in hands:
        xval = hand_rank(x)
        if not result or xval > max_val:
            result, max_val = [x], xval
        elif xval == max_val:
            result.append(x)
    return result


def hand_rank(hand):
    groups = group(['--234567891JQKA'.index(r[0]) for r in hand.split()])
    counts, ranks = zip(*groups)
    if ranks == (14, 5, 4, 3, 2): ranks = (5, 4, 3, 2, 1)
    straight = len(counts) == 5 and max(ranks) - min(ranks) == 4
    flush = len(set([s[-1] for s in hand.split()])) == 1
    return (8 if straight and flush else
            7 if counts == (4, 1) else
            6 if counts == (3, 2) else
            5 if flush else
            4 if straight else
            3 if counts == (3, 1, 1) else
            2 if counts == (2, 2, 1) else
            1 if counts == (2, 1, 1, 1) else
            0, ranks)


def group(items):
    groups = [(items.count(x), x) for x in set(items)]
    return sorted(groups, reverse=True)
