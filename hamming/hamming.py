def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError(".+")
    
    hamming_distance = 0

    for i in range(len(strand_b)):
        if strand_a[i] != strand_b[i]:
            hamming_distance += 1

    return hamming_distance
