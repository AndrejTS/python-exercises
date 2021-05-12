import re
from operator import add, mul, sub, floordiv


dict_func = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': floordiv
}


def answer(question):
    question = re.sub('What is ', '', question)
    question = re.sub('plus', '+', question)
    question = re.sub('minus', '-', question)
    question = re.sub('multiplied by', '*', question)
    question = re.sub('divided by', '/', question)
    question = re.sub(r'\?', '', question)
    question = question.split()

    # if the length is even, the input is invalid
    if len(question) % 2 == 0:
        raise ValueError('Invalid input!')
    # check rotation
    for i in range(len(question)):
        if i % 2 == 0: # even must be number
            if re.sub('-?[0-9]+', '', question[i]):
                raise ValueError('Invalid input!')                
        elif question[i] not in ['+', '-', '*', '/']: # odd must be operation
            raise ValueError('Invalid input!')

    # What is 5?
    if len(question) == 1:
        return int(question[0])

    # processing first operation, for example: What is 5 plus 2?
    value = helper(question[0], question[1], question[2])
    # continue if question is longer, for example: What is 3 plus 7 multiplied by 2?
    for i in range(3, len(question), 2):
        value = helper(value, question[i], question[i+1])

    return value


def helper(first, operation, second):
    operation = dict_func[operation]
    return operation(int(first), int(second))

