def is_armstrong_number(number):
    number = str(number) 
    return int(number) == sum([int(i) ** len(number) for i in number])
