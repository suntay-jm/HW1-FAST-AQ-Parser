from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe)

def main():
    """
    The main function
    """
    # Create instance of FastaParser
    fasta = FastaParser("data/test.fa")
    
    # Create instance of FastqParser
    fastq = FastqParser("data/test.fq")
        
    # For each record of FastaParser, Transcribe the sequence
    # and print it to console
    for header, seq in fasta:
        transcribed_seq = transcribe(seq)
        print(f">{header}\n{transcribed_seq}")

    print("====== switching to fastq ======")
       
    # For each record of FastqParser, Transcribe the sequence
    # and print it to console
    for header, seq, quality in fastq:
        transcribed_seq = transcribe(seq)
        print(f"@{header}\n{transcribed_seq}")

    print("====== switching to reverse fasta ======")

    # For each record of FastaParser, Reverse Transcribe the sequence
    # and print it to console

    for header, seq in fasta:
        reverse_transcribed_seq = reverse_transcribe(seq)
        print(f">{header}_reversed\n{reverse_transcribed_seq}")

    print("====== switching to reverse fastq ======")
    
    # For each record of FastqParser, Reverse Transcribe the sequence
    # and print it to console
    
    for header, seq, quality in fastq:
        reverse_transcribed_seq = reverse_transcribe(seq)
        print(f"@{header}_reversed\n{reverse_transcribed_seq}")


"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main()
