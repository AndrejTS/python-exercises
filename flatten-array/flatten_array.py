def flatten(iterable):
    result = []
    for i in iterable:
        if type(i) == list:
            for k in flatten(i):
                result.append(k)
        elif i != None:
            result.append(i)
    return result
