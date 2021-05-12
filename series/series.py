def slices(string, length):
    if not 1 <= length <= len(string):
        raise ValueError("Bad length value: " + str(length))
    result = []
    for i in range(len(string)):
        serie = ''
        for k in range(length):
            try:
                serie += string[i + k]
            except:
                break
        if len(serie) == length:
            result.append(serie)
    return result
