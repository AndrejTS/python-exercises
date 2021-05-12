import re

def abbreviate(words):
    result = ""
    words = re.findall("[a-z]+'[a-z]+|[a-z]+", words.lower())
    for word in words:
        result += word[0].upper()
    return result
    