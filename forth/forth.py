class StackUnderflowError(Exception):
    pass


integer_arithmetic = {
    '-': lambda x, y: y - x,
    '+': lambda x, y: y + x,
    '*': lambda x, y: y * x,
    '/': lambda x, y: y // x
}


stack_manipulation = {
    'DUP': lambda s: s + [s[-1]] if len(s) > 0 else None,
    'DROP': lambda s: s[:-1] if len(s) > 0 else None,
    'SWAP': lambda s: s[:-2] + [s[-1], s[-2]] if len(s) > 1 else None,
    'OVER': lambda s: s + [s[-2]] if len(s) > 1 else None
}


def add_definition(string, added_words):
    definition = string.split()
    definition = definition[1:-1]
    key = definition[0]
    value = definition[1:]
    if key.isdigit():
        raise ValueError('cannot_redefine_numbers')
    for k in range(len(value)):
        while value[k].upper() in added_words:
            value[k] = added_words[value[k].upper()]
    return (key.upper(), ' '.join(value).upper())


def evaluate(input_data):
    added_words = dict()
    for line in input_data:
        if line[0] == ':':
            key, value = add_definition(line, added_words)
            added_words[key] = value
    while input_data[0][:1] == ':':
        input_data.pop(0)

    expression = input_data[0].upper()
    for word in added_words:
        expression = expression.replace(word, added_words[word])

    stack = []
    for item in expression.split():
        try:
            if item.isdigit():
                stack.append(int(item))
            elif item in integer_arithmetic:
                x = stack.pop()
                y = stack.pop()
                stack.append(integer_arithmetic[item](x, y))
            elif item in stack_manipulation:
                if stack_manipulation[item](stack) is None:
                    raise StackUnderflowError
                stack = stack_manipulation[item](stack)
            else:
                raise ValueError('non_existent_word')
        except (IndexError, StackUnderflowError):
            raise StackUnderflowError("Insufficient number of items in stack")
    return stack

