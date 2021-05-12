def proteins(strand):
    d = {
        'AUG': 'Methionine',
        'UUC': 'Phenylalanine',
        'UUU': 'Phenylalanine',
        'UUG': 'Leucine',
        'UUA': 'Leucine',
        'UCU': 'Serine',
        'UCC': 'Serine',
        'UCA': 'Serine',
        'UCG': 'Serine',
        'UAC': 'Tyrosine',
        'UAU': 'Tyrosine',
        'UGC': 'Cysteine',
        'UGU': 'Cysteine',
        'UGG':	'Tryptophan'
    }
    output = []
    for i in range(0, len(strand), 3):
        if strand[i:i+3] in ['UAA', 'UAG', 'UGA', 'STOP']:
            break
        output.append(d[strand[i:i+3]])
    return output

