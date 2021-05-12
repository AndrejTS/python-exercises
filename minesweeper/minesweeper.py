import itertools


neighbors = list(itertools.product((-1, 0, 1), (-1, 0, 1)))


def annotate(minefield):
    verify_board(minefield)
    result = []
    for row in range(len(minefield)):
        line = ''
        for col in range(len(minefield[0])):
            if minefield[row][col] == '*':
                line += '*'
            else:
                count = count_mines(minefield, row, col)
                if count != 0:
                    line += str(count)
                else:
                    line += ' '
        result.append(line)
    return result


def verify_board(minefield):
    for row in minefield:
        if len(row) != len(minefield[0]):
            raise ValueError('Incorrect minefield size')
        if set(row) - {' ', '*'}:
            raise ValueError('Only spaces and asterisks can by passed')
        

def count_mines(minefield, row, col):
    max_r = len(minefield) - 1
    max_c = len(minefield[0]) - 1
    count = 0
    for i in neighbors:
        r = row + i[0]
        c = col + i[1]
        if r < 0 or r > max_r or c < 0 or c > max_c: 
            continue
        if minefield[r][c] == '*':
            count += 1
    return count

