from itertools import zip_longest


def transpose(lines):
    lines = lines.split('\n')
    transposed = list(zip_longest(*lines))
    rows = []
    for i in transposed:
        row = ''
        for k in range(len(i)):
            try:
                row += i[k]
            except TypeError:
                if any([True for x in i[k:] if x != None]):
                    row += ' '
                else:
                    break
        rows.append(row)

    return '\n'.join(rows)
