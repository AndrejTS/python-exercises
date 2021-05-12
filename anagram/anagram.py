def find_anagrams(word, candidates):
    result = []
    for candidate in candidates:
        if candidate.upper() == word.upper():
            continue
        if sorted(candidate.upper()) == sorted(word.upper()):
            result.append(candidate)
    return result
