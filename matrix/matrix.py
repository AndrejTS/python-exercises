class Matrix:
    def __init__(self, matrix_string):
        self.rows = []
        for row in matrix_string.split('\n'):
            self.rows.append([int(n) for n in row.split()])

        self.columns = []
        for col in zip(*self.rows):
            self.columns.append(list(col))

    def row(self, n):
        return self.rows[n-1]

    def column(self, n):
        return self.columns[n-1]

