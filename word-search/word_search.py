# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y


# class WordSearch:
#     def __init__(self, puzzle):
#         self.puzzle = puzzle

#     def search(self, word):
#         for y in range(len(self.puzzle)):
#             for x in range((len(self.puzzle[0]))):
#                 if self.puzzle[y][x] != word[0]:
#                     continue
#                 if self.function(x, y, word):
#                     last_x, last_y = self.function(x, y, word)
#                     return Point(x, y), Point(last_x, last_y)
    
#     def function(self, x, y, word):
#         if self.puzzle[y][x] == word:
#             return x, y
#         # left-to-right
#         for i in range(x+1, len(self.puzzle[0])):
#             try:
#                 if self.puzzle[y][x:x+i] == word:
#                     return x + i - 1, y
#             except:
#                 break
#         # right-to-left
#         if self.puzzle[y][x::-1] == word:
#             return 0, y
#         for i in range(x-1, -1, -1):
#             try:
#                 if self.puzzle[y][x:i:-1] == word:
#                     return i + 1, y
#             except:
#                 break
#         # vertical-down
#         chunk = self.puzzle[y][x]
#         for i in range(y+1, len(self.puzzle)):
#             try:
#                 chunk += self.puzzle[y+i][x]
#                 if chunk == word:
#                     return x, y + i
#             except:
#                 break
#         # vertical-up
#         chunk = self.puzzle[y][x]
#         for i in range(y-1, -1, -1):
#             try:
#                 chunk += self.puzzle[i][x]
#                 if chunk == word:
#                     return x, i
#             except:
#                 break
#         # diagonal-to-right-down
#         chunk = self.puzzle[y][x]
#         for i in range(1, len(self.puzzle[0])):
#             try:
#                 chunk += self.puzzle[y+i][x+i]
#                 if chunk == word:
#                     return x + i, y + i
#             except:
#                 break
#         # diagonal-to-right-up
#         chunk = self.puzzle[y][x]
#         for i in range(1, len(self.puzzle[0])):
#             try:
#                 chunk += self.puzzle[y-i][x+i]
#                 if chunk == word:
#                     return x + i, y - i
#             except:
#                 break
#         # diagonal-to-left-down
#         chunk = self.puzzle[y][x]
#         for i in range(1, len(self.puzzle[0])):
#             try:
#                 chunk += self.puzzle[y+i][x-i]
#                 if chunk == word:
#                     return x - i, y + i
#             except:
#                 break
#         # diagonal-to-left-up
#         chunk = self.puzzle[y][x]
#         for i in range(1, len(self.puzzle[0])):
#             try:
#                 chunk += self.puzzle[y-i][x-i]
#                 if chunk == word:
#                     return x - i, y - i
#             except:
#                 break

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch:
    directions = [
        (1, 0), 
        (-1, 0), 
        (0, 1), 
        (0, -1), 
        (1, 1), 
        (1, -1), 
        (-1, 1), 
        (-1, -1)
    ]

    def __init__(self, puzzle):
        self.puzzle = puzzle

    def search(self, word):
        for y in range(len(self.puzzle)):
            for x in range((len(self.puzzle[0]))):
                if self.puzzle[y][x] != word[0]:
                    continue
                else:
                    for d in self.directions:
                        chunk = self.puzzle[y][x]
                        x2 = x
                        y2 = y
                        while True:
                            try:
                                if chunk == word:
                                    return Point(x, y), Point(x2, y2)
                                x2 += d[0]
                                y2 += d[1]
                                chunk += self.puzzle[y2][x2]
                            except:
                                break
