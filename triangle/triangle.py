def is_triangle(func):
    def wrapper(sides):
        for side in sides:
            if side == 0:
                return False
        if sides[0] + sides[1] < sides[2]: return False
        if sides[0] + sides[2] < sides[1]: return False
        if sides[1] + sides[2] < sides[0]: return False
        return func(sides)
    return wrapper


@is_triangle
def equilateral(sides):
    if len(set(sides)) == 1:
        return True
    return False


@is_triangle
def isosceles(sides):
    if len(set(sides)) < 3:
        return True
    return False


@is_triangle
def scalene(sides):
    if len(set(sides)) == 3:
        return True
    return False

