WHITE = 'W'
BLACK = 'B' 
NONE = ' '


class Board:
    def __init__(self, board):
        self.board = board


    def territory(self, x, y):
        if x < 0 or y < 0:
            raise ValueError(' ')
        if x >= len(self.board[0]) or y >= len(self.board):
            raise ValueError(' ')
        if self.board[y][x] != ' ':
            return (' ', set())
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        territory = [(x, y)]
        neighbours = []
        for t in territory:
            for d in directions:
                xd = t[0] + d[0]
                yd = t[1] + d[1]
                if xd >= 0 and yd >= 0:
                    try:
                        if self.board[yd][xd] == ' ':
                            if (xd, yd) not in territory:
                                territory.append((xd, yd))
                        else:
                            neighbours.append(self.board[yd][xd])
                    except:
                        continue
        if len(set(neighbours)) == 1:
            return (neighbours[0], set(territory))
        else:
            return (' ', set(territory))


    def territories(self):
        result = {BLACK: set(), WHITE: set(), NONE: set()}
        for j in range(len(self.board[0])):
            for k in range(len(self.board)):
                stone, territory = self.territory(j, k)
                result[stone].update(territory)
        return result

