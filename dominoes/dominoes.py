from itertools import permutations


def can_chain(dominoes):
    if not dominoes:
        return []
    if len(dominoes) == 1: 
        if dominoes[0][0] == dominoes[0][1]:
            return dominoes
        else:
            return None
    
    for possibility in permutations(dominoes):
        possibility = list(possibility)
        for stone in range(len(possibility)):
            if stone == len(possibility)-1:
                if possibility[0][0] == possibility[-1][1]:
                    return possibility 
                else:
                    break
            if possibility[stone][1] == possibility[stone+1][0]:
                continue
            if possibility[stone][1] == possibility[stone+1][1]:
                possibility[stone+1] = possibility[stone+1][::-1]
                continue
            else:
                break

