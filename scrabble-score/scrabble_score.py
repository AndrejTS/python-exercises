def score(word):
    score = 0
    values = [
                ["A, E, I, O, U, L, N, R, S, T", 1],
                ["D, G", 2],
                ["B, C, M, P", 3],
                ["F, H, V, W, Y", 4],
                ["K", 5],
                ["J, X", 8],
                ["Q, Z", 10]
    ]

    for letter in word.upper():
        for i in range(len(values)):
            if letter in values[i][0]:
                score += values[i][-1]
                break
    return score