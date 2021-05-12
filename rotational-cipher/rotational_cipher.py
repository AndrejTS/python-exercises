def rotate(text, key):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for i in text:
        if i in letters:
            index = (letters.find(i) + key) % 26
            result += letters[index]
        elif i in letters.upper():
            index = (letters.find(i.lower()) + key) % 26
            result += letters[index].upper()
        else:
            result += i
            
    return result
