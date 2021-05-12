# Globals for the directions
# Change the values as you see fit
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.x = x
        self.y = y
        self.direction = direction
        self.coordinates = (self.x, self.y)


    def move(self, instructions):
        for i in instructions:
            if i == 'A':
                if self.direction == 0: self.y += 1
                if self.direction == 1: self.x += 1
                if self.direction == 2: self.y -= 1
                if self.direction == 3: self.x -= 1
                self.coordinates = (self.x, self.y)
            else:
                if i == 'R': self.direction += 1 
                elif i == 'L': self.direction -= 1 
                self.direction %= 4

