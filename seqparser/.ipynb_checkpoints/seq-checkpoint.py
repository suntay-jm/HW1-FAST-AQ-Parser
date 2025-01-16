# DNA -> RNA Transcription

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}

def transcribe(dna_string):
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    transcribed = ""
    for nt in dna_string:
        transcribed += TRANSCRIPTION_MAPPING[nt]
    return transcribed

def reverse_transcribe(dna_string):
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    rev_comp = ""
    for nt in dna_string[::-1]:
        rev_comp += TRANSCRIPTION_MAPPING[nt]
    return rev_comp
