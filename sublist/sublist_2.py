SUBLIST = 'SUBLIST'
SUPERLIST = 'SUPERLIST'
EQUAL = 'EQUAL'
UNEQUAL = 'UNEQUAL'


def sublist(list_one, list_two):
    list_one = [str(item) for item in list_one]
    list_one = '-'.join(list_one)
    list_two = [str(item) for item in list_two]
    list_two = '-'.join(list_two)
    if list_one == list_two:
        return EQUAL
    elif list_one in list_two:
        return SUBLIST
    elif list_two in list_one:
        return SUPERLIST
    else:
        return UNEQUAL

