def value(colors):
    result = ''
    values = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
    }
    for i in range(2):
        result += str(values[colors[i]])
    return int(result)

