from collections import Counter


PER_BOOK = 800.00
PER_GROUP = {
    0: 0,
    1: 1 * PER_BOOK * 1.00,
    2: 2 * PER_BOOK * 0.95,
    3: 3 * PER_BOOK * 0.90,
    4: 4 * PER_BOOK * 0.80,
    5: 5 * PER_BOOK * 0.75,
}


def total(books):
    volumes = Counter(books)
    num_books, num_volumes = len(books), len(volumes)
    price = num_books * PER_BOOK
    for group in range(num_volumes, 1, -1):
        # group to remove => gtr
        gtr = Counter(k for k, _ in volumes.most_common(group))
        residue = volumes - gtr
        residue = list(residue.elements())
        price = min(price, PER_GROUP[group] + total(residue))
    return price

