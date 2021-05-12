animals = [
    None, 
    'fly', 
    'spider', 
    'bird', 
    'cat', 
    'dog', 
    'goat', 
    'cow', 
    'horse'
]

unique = [
    None,
    None,
    "It wriggled and jiggled and tickled inside her.",
    "How absurd to swallow a bird!",
    "Imagine that, to swallow a cat!",
    "What a hog, to swallow a dog!",
    "Just opened her throat and swallowed a goat!",
    "I don't know how she swallowed a cow!",
    "She's dead, of course!"
]

know = "I know an old lady who swallowed a {}."
swallowed = "She swallowed the {} to catch the {}."
dont_know = "I don't know why she swallowed the fly. Perhaps she'll die."


def recite(start_verse, end_verse):
    result = []
    for i in range(start_verse, end_verse+1):
        result.append(know.format(animals[i]))
        if unique[i]:
            result.append(unique[i])
        if i != 8:
            for k in range(i, 1, -1):
                first = animals[k]
                second = animals[k-1]
                if k == 3:
                    second += ' that' + unique[2][2:-1]
                result.append(swallowed.format(first, second))
            result.append(dont_know)
        if i != end_verse:
            result.append('')
    return result
