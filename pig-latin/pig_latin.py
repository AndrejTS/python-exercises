import re

re_vowel = re.compile('^([aeiou]|yt|xr)')
re_cons = re.compile('^([^aeiou]?qu|[^aeiouy]+|y(?=[aeiou]))([a-z]*)')

def starts_with_vowel_sound(word):
    return re_vowel.match(word) is not None

def split_initial_consonant_sound(word):
    return re_cons.match(word).group(1, 2)

def translate(text):
    output = ''
    for word in text.split():
        if starts_with_vowel_sound(word):
            output += (word + 'ay ')
        else:
            head, tail = split_initial_consonant_sound(word)
            output += (tail + head + 'ay ')
    return output.rstrip(' ')

