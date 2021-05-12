pattern = [
    [" _ ", "| |", "|_|", "   "],
    ["   ", "  |", "  |", "   "],
    [" _ ", " _|", "|_ ", "   "],
    [" _ ", " _|", " _|", "   "],
    ["   ", "|_|", "  |", "   "],
    [" _ ", "|_ ", " _|", "   "],
    [" _ ", "|_ ", "|_|", "   "],
    [" _ ", "  |", "  |", "   "],
    [" _ ", "|_|", "|_|", "   "],
    [" _ ", "|_|", " _|", "   "]
]


def convert(input_grid):
    if len(input_grid) % 4 != 0 or len(input_grid[0]) % 3 != 0:
        raise ValueError(' ')
    result = ""
    for section in range(0, len(input_grid), 4):
        for col in range(0, len(input_grid[0]), 3):
            number = []
            for row in range(4):
                r = row + section
                c = col
                number.append(input_grid[r][c:c+3])
            if number in pattern:
                result += str(pattern.index(number))
            else:
                result += '?'
        result += ','
    return result[:-1]

