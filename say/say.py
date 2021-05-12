num_to_words = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 
    15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 
    18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 
    40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 
    80: 'eighty', 90: 'ninety'
}


def say(number):
    if not 0 <= number < 1e12:
        raise ValueError(' ')
    if number == 0:
        return 'zero'
        
    number = str(number)
    chunks = [] 
    # breaking a number into chunks of thousands
    for i in range(0, 13, 3):
        if number[-3:] != '':
            chunks.insert(0, number[-3:])
            number = number[:-3]
        else:
            break

    bigs = ['', 'thousand', 'million', 'billion']
    bigs_cur_index = len(chunks) - 1
    result = []
    for i in chunks:
        if int(i) != 0:
            chunk = func(int(i)) + ' ' + bigs[bigs_cur_index]
            result.append(chunk)  
        bigs_cur_index -= 1

    return " ".join(result).rstrip()


# function to convert a three-digit number to text
# e.g. 321 => three hundred twenty-one
def func(n):
    if n >= 100:
        return num_to_words[n // 100] + ' hundred ' + func(n % 100)
    elif n >= 20:
        output = num_to_words[(n // 10) * 10]
        if n % 10 != 0:
            output += '-' + num_to_words[n % 10]
        return output 
    elif n > 0:
        return num_to_words[n]
    else:
        return ''
