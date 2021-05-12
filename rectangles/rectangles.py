from itertools import combinations


def rectangles(strings):
    if len(strings) == 0:
        return 0
    y_size = len(strings)
    x_size = len(strings[0])
    vertices = []
    for y in range(y_size):
        for x in range(x_size):
            if strings[y][x] == '+':
                vertices.append((y, x))
    combs = combinations(vertices, 4)
    count = 0     
    for r in combs:
        if (
            check_line(strings, r[0], r[1], 'x') and 
            check_line(strings, r[2], r[3], 'x') and 
            check_line(strings, r[0], r[2], 'y') and 
            check_line(strings, r[1], r[3], 'y')
        ):
            count += 1
    return count


def check_line(strings, point1, point2, direction):
    if direction == 'x': index = 0
    if direction == 'y': index = 1
    if point1[index] != point2[index]:
        return False
    
    for x in range(point1[1], point2[1]):
        if strings[point1[0]][x] not in ('-', '+'):
            return False
    for y in range(point1[0], point2[0]):
        if strings[y][point1[1]] not in ('|', '+'):
            return False
    return True

