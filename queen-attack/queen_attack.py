class Queen:
    def __init__(self, row, column):
        if (0 > row or row > 7) or (0 > column or column > 7):
            raise ValueError('Bad input')
        self.row = row
        self.column = column


    def can_attack(self, another_queen):
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError('No, no, no') 
        if self.row == another_queen.row or self.column == another_queen.column:
            return True
        if abs(self.row - another_queen.row) == abs(self.column - another_queen.column):
            return True
        return False
