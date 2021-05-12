import math


def find(search_list, value):
    start = 0
    end = len(search_list) - 1
    while start <= end:
        middle = math.ceil((start + end) / 2)
        if search_list[middle] == value:
            return middle
        if search_list[middle] < value:
            start = middle + 1
        if search_list[middle] > value:
            end = middle - 1
    raise ValueError("Value not found.")

