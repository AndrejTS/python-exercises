SUBLIST = 'SUBLIST'
SUPERLIST = 'SUPERLIST'
EQUAL = 'EQUAL'
UNEQUAL = 'UNEQUAL'


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    elif contains(list_one, list_two):
        return SUBLIST
    elif contains(list_two, list_one):
        return SUPERLIST
    return UNEQUAL


def contains(sub, _super):
    if sub == []:
        return True

    for i in range(len(_super)):
        if _super[i] == sub[0]:
            matches = 0
            for k in range(len(sub)):
                try:
                    if _super[i + k] == sub[k]:
                        matches += 1
                except IndexError:
                    return False
            if matches == len(sub):
                return True

    return False

