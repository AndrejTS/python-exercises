from itertools import cycle


def spiral_matrix(size):
    matrix = [[None for i in range(size)] for k in range(size)]
    row, col = 0, 0
    d = cycle([(0, 1), (1, 0), (0, -1), (-1, 0)])
    drow, dcol = next(d)
    
    for number in range(1, (size ** 2 + 1)):
        matrix[row][col] = number
        if (
            col + dcol < 0 or
            col + dcol == size or 
            row + drow == size or
            matrix[row + drow][col + dcol] is not None
        ):
            drow, dcol = next(d)
        row += drow
        col += dcol
    return matrix
