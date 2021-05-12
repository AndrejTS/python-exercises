from math import ceil


def cipher_text(text):
    text = ''.join(filter(str.isalnum, text.lower()))
    col = ceil(len(text) ** 0.5)
    if col * (col - 1) >= len(text):
        row = col - 1
    else: 
        row = col

    rectangle = []
    for _ in range(row):
        rectangle.append(text[:col].ljust(col))
        text = text[col:]

    unzipped = zip(*rectangle)
    chunks = []
    for chunk in unzipped:
        chunks.append(''.join(chunk))
    return ' '.join(chunks) 

