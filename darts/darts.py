def score(x, y):
    diagonal = (x**2 + y**2) ** 0.5
    if diagonal <= 1:
        return 10
    if diagonal <= 5:
        return 5
    if diagonal <= 10:
        return 1
    else:
        return 0
