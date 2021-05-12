def check_connection(strings, y1, y2, x1, x2):
    for x in range(x1 + 1, x2):
        if strings[y1][x] != '-' and strings[y1][x] != '+':
            return False
    for y in range(y1 + 1, y2):
        if strings[y][x1] != '|' and strings[y][x1] != '+':
            return False
    return True


def rectangles(strings):
    if len(strings) == 0:
        return 0
    count = 0
    y_size = len(strings)
    x_size = len(strings[0])
    for y in range(y_size):
        for x in range(x_size):
            if strings[y][x] == '+':
                for i in range(x+1, x_size):
                    if strings[y][i] == '+':
                        if not check_connection(strings, y, y, x, i):
                            break
                        for k in range(y+1, y_size):
                            if strings[k][i] == '+':
                                if not check_connection(strings, y, k, i, i):
                                    break
                                if strings[k][x] == '+':
                                    if not check_connection(strings, k, k, x, i):
                                        break
                                    if not check_connection(strings, y, k, x, x):
                                        break
                                    count += 1
    return count


