from string import ascii_uppercase


def solve(puzzle):
    output = {}
    numbers = to_numbers(puzzle)
    if numbers == None:
        return None
    for i in range(len(puzzle)):
        if puzzle[i] in ascii_uppercase:
            output[puzzle[i]] = int(numbers[i])
    return output


def to_numbers(string):
    for i in range(len(string)):
        if string[i] in ascii_uppercase:
            letter = string[i]
            break
    for n in range(10):
        if str(n) in string:
            continue
        shot = string.replace(letter, str(n))
        if set(ascii_uppercase) & set(shot):
            for x in ascii_uppercase:
                if x in shot:
                    if to_numbers(shot):
                        return to_numbers(shot)
        try:
            if eval(shot) == True:
                if shot.split()[-1][0] != '0':
                    return shot
        except:
            continue

#####################

from itertools import permutations
import re


def solve(puzzle):
    f, letters = compile_formula(puzzle)
    for digits in fill_in(letters):
        if f(*digits):
            table = letters.maketrans(letters, ''.join(map(str, digits)))
            filled = puzzle.translate(table)
            if not re.search(r'\b0[0-9]', filled):
                result = dict(zip(letters, digits))
                return result
        

def compile_formula(formula):
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    parms = ', '.join(letters)
    tokens = map(compile_word, re.split('([A-Z]+)', formula))
    body = ''.join(tokens)
    f = f'lambda {parms}: {body}'
    return eval(f), letters


def compile_word(word):
    if word.isupper():
        terms = [(f'{10**i}*{d}') for (i, d) in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'
    else:
        return word


def fill_in(letters):
    for digits in permutations('1234567890', len(letters)):
        table = letters.maketrans(letters, ''.join(digits))
        filled = letters.translate(table)
        output = []
        for i in filled:
            output.append(int(i))
        yield output

