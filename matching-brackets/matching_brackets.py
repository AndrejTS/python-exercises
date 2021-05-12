def is_paired(input_string):
    brackets_pairs = {
        '[': ']',
        '{': '}',
        '(': ')'
    }
    stack = []
    for i in input_string:
        if i in brackets_pairs:
            stack.append(i)
        elif i in brackets_pairs.values():
            if stack == [] or i != brackets_pairs[stack.pop()]:
                return False
    return stack == []




#### first version
    s = input_string
    for b in ['[]', '{}', '()']:
        if s.count(b[0]) != s.count(b[1]):
            return False
    
    brackets_list = []
    for i in input_string:
        if i in '[]{}()':
            brackets_list.append(i)

    for i in range(len(brackets_list) - 1):
        if brackets_list[i] == '[' and brackets_list[i + 1] in '})':
            return False
        if brackets_list[i] == '{' and brackets_list[i + 1] in '])':
            return False
        if brackets_list[i] == '(' and brackets_list[i + 1] in ']}':
            return False

    if brackets_list:
        if brackets_list[0] in ']})' or brackets_list[-1] in '[{(':
            return False
            
    return True
    
