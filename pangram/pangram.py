def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    indexes = set()
    for letter in sentence:
        index = alphabet.find(letter.lower())
        if index != -1:
            indexes.add(index)
    if len(indexes) == 26:
        return True
    return False
    