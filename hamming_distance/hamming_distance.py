def hamming_distance(sequence1: str, sequence2: str, verbose:bool = False) -> int:
    """
    Measures hamming distance between 2 sequences.
    
    Example:
    >>> hamming_distance("AGC", "ATC", verbose=True)
    Hamming distance: 1
    """
    # Check if sequences are of equal length
    if len(sequence1) != len(sequence2):
            raise ValueError("Sequences must be of equal length")
        
    hamming_dist = 0
    for i in range(len(sequence1)):
        if sequence1[i] != sequence2[i]:
            hamming_dist += 1
    # Print resulting hamming distance        
    if verbose:
        print(f"Hamming distance: {hamming_dist}")
    
    return hamming_dist