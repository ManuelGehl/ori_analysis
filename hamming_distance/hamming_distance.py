def hamming_distance(sequence1: str, sequence2: str, verbose:int = 0) -> int:
    """
    Measures hamming distance between 2 sequences.
    """
    # Check if sequences are of equal length
    if len(sequence1) != len(sequence2):
            raise ValueError("Sequences must be of equal length")
        
    hamming_dist = 0
    for i in range(len(sequence1)):
        if sequence1[i] != sequence2[i]:
            hamming_dist += 1
    if verbose == 1:
        print(f"Hamming distance: {hamming_dist}")
    
    return hamming_dist


seq1 = "TGTGAGAGTGGT"
seq2 = "ACCTCGAATAGT"

hamming_distance(seq1, seq2)