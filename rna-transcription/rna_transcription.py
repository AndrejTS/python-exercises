def to_rna(dna_strand):
    transcription = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    rna = ""
    for i in dna_strand:
        rna += transcription[i]
    return rna
