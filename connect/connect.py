class ConnectGame:
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1), (-1, 1), (1, -1)]

    def __init__(self, board):
        self.board = [[]]
        y = 0
        for i in board:
            if i in '.XO':
                self.board[y].append(i)
            if i == '\n':
                self.board.append([])
                y += 1

    def get_winner(self):
        if self.check_connect('X'):
            return 'X'
        if self.check_connect('O'):
            return 'O'
        return ''

    def check_connect(self, player):
        if player == 'X':
            board = list(zip(*self.board))
        else:
            board = self.board
        stones = list() # start with one side
        for i in range(len(board[0])):
            if board[0][i] == player:
                stones.append((0, i))
        for stone in stones: # finding paths
            for d in self.directions:
                y = stone[0] + d[0]
                x = stone[1] + d[1]
                if x >= 0 and y >= 0:
                    try:
                        if board[y][x] == player:
                            if (y, x) not in stones:
                                stones.append((y, x))
                    except:
                        continue
        for s in stones: # check connection
            if s[0] == len(board) - 1:
                return True


