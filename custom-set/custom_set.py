class CustomSet(set):
    def isempty(self):
        return len(self) == 0

    def __add__(self, other):
        return self | other
