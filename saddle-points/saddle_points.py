def saddle_points(matrix):
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError('Irregular matrix!')

    candidates = [] 
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] >= max(matrix[row]):
                candidates.append((row, col))

    results = []
    for can in candidates:
        can_row = can[0]
        can_col = can[1]
        saddle = 1
        for i in range(len(matrix)):
            if matrix[i][can_col] < matrix[can_row][can_col]:
                saddle = False
                break
        if saddle: 
            results.append({"row": can_row + 1, "column": can_col + 1})

    return results

