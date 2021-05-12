def append(list1, list2):
    return list1 + list2


def concat(lists):
    result = []
    for i in lists:
        result += i
    return result


def filter(function, list):
    result = []
    for i in list:
        if function(i) == True:
            result += [i]
    return result


def length(list):
    result = 0
    for _ in list:
        result += 1
    return result


def map(function, list):
    result = []
    for i in list:
        result += [function(i)]
    return result


def foldl(function, list, initial):
    result = initial
    for i in list:
        result = function(result, i)
    return result


def foldr(function, list, initial):
    result = initial
    for i in list[::-1]:
        result = function(i, result)
    return result


def reverse(list):
    return list[::-1]

