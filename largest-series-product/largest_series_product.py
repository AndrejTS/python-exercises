def largest_product(series, size):
    if size == 0:
        return 1
    if not 1 <= size <= len(series):
        raise ValueError("Bad input")
    max = 0
    for i in range(len(series)):
        chunk = int(series[i])
        for k in range(1, size):
            try:
                chunk *= int(series[i + k])
            except:
                chunk = 0
                break
        if chunk > max: 
            max = chunk
    return max
