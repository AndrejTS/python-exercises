this = [
    "house that Jack built.",
    "malt",
    "rat",
    "cat",
    "dog",
    "cow with the crumpled horn",
    "maiden all forlorn",
    "man all tattered and torn",
    "priest all shaven and shorn",
    "rooster that crowed in the morn",
    "farmer sowing his corn",
    "horse and the hound and the horn"
]

that = [
"belonged to",
"kept",
"woke",
"married",
"kissed",
"milked",
"tossed",
"worried",
"killed",
"ate",
"lay in",
]

def recite(start_verse, end_verse):
    result = []
    for i in range(start_verse - 1, end_verse):
        result.append(verse(i))
    return result

def verse(n):
    verse = f'This is the {this[n]}'
    for k in range(n, 0, -1):  
        verse += f' that {that[-k]} the {this[k-1]}'
    return verse
