def recite(start, take=1):
    result = []
    for i in range(take):
        num_bottles = start - i
        if num_bottles > 2:
            result.append("{0} bottles of beer on the wall, {0} bottles of beer.".format(num_bottles))
            result.append("Take one down and pass it around, {0} bottles of beer on the wall.".format(num_bottles - 1))
        elif num_bottles == 2:
            result.append("2 bottles of beer on the wall, 2 bottles of beer.")
            result.append("Take one down and pass it around, 1 bottle of beer on the wall.")
        elif num_bottles == 1:
            result.append("1 bottle of beer on the wall, 1 bottle of beer.")
            result.append("Take it down and pass it around, no more bottles of beer on the wall.")
        elif num_bottles == 0:
            result.append("No more bottles of beer on the wall, no more bottles of beer.")
            result.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
        if i < take - 1:
            result.append('')
    return result


