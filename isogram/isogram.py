import string
punctuation = string.punctuation + " "

def is_isogram(string):
    string = string.lower()
    for l in string:
        if string.count(l) > 1:
            if l not in punctuation:
                return False
    return True
