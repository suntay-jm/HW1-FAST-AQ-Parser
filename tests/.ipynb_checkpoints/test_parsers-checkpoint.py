# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest
# assert will be used here: assert condition, "Error message"
# if condition is met, test passes and nothing happens
# else, test failes and error message is displayed


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    bad_parser = FastaParser("./bad.fa") # making an instance of the FastaParser class using bad.fa

    # bad.fa has no sequences which will raise a ValueError
    # using pytest.raises to check for expected errors -- passes if expected error gets raised, fails if it doesn't 

    """
    parse.py creates the error:Parser class -> __iter__(self) -> if nseq == 0 (meaning no seqs): raise ValueError  
    pytest looks out for that ValueError
    """
    with pytest.raises(ValueError):
        records = list(bad_parser) # forces parser to process file and convert all records into a list --> triggers error (no seqs)

    good_parser = FastaParser("../data/test.fa") # going back one directory and into the data directory
    records = list(good_parser) # __iter__ method of FastaParser reads file and gets all the records one by one and puts them in a list

    """
    records will look like:
    [("seq1", "sequence_here"), ("seq2", "sequence2_here)]
    """

    # there's 99 seqs, so if there's only 2 seqs, then FastaParser didn't get the right number of seqs
    assert len(records) == 100, "incorrect number of seqs"

    # checks if seqs read as tuple 
    assert isinstance(records[0], tuple), "not read as a tuple" # isinstance() checks if value is a specified type


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    check_fasta = FastaParser("../data/test.fq")
    records = list(check_fasta) # converting to list to check first element

    assert records[0] is not None, "first item isn't None"

def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    good_fastq = FastqParser("../data/test.fq") 
    records = list(good_fastq)
    """
    records would look like:
    [(
        "seq0",
        "TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG",
     "*540($=*,=.062565,2>'487')!:&&6=,6,*7>:&132&83*8(58&59>'8!;28<94,0*;*.94**:9+7\"94(>7='(!5\"2/!%\"4#32="
    ),
    (
        "seq1",
        "CCCCGGACGACTGATCCCGATAGAGCTCACTCTTCGAGGCAAGCAGACCCATATCGTCCTGCTGGCAACGCTATCCGGGTGCGAGTAAATCGAAACCTCG",
        "'(<#/0$5&!$+,:=%7=50--1;'(-7;0>=$(05*9,,:%0!<),%646<8#%\".\"-'*-0:.+*&$5!'8)(%3*+9/&/%=363*,6$20($97,\""
    )]
    """
    assert len(records) > 0, "nothing was read in" 
    assert records[0][1] is not None, "seq not read in correctly" 
    assert records[0][2] is not None, "quality not read in correctly"
    

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    bad_fastq = FastqParser("../data/test.fa")
    records = list(bad_fastq)
    assert records[0] is not None, "first item isn't None"