def generate_k_mers(sequence: str, k_mer_length: int, seq_range: tuple = (0, 100)) -> list:
    
    # Define part of sequence to generate k-mers from
    start, stop = seq_range
    # Check if sequence range lies within the sequence
    # TO DO
    sequence_part = sequence[start:stop + 1]
    
    # Define scanning range
    scanning_range = len(sequence_part) - k_mer_length + 1
    
    k_mers = set()
    # Slide a window over the sequence part
    for pos in range(scanning_range):
        # Add current k-mer to list
        k_mers.add(sequence_part[pos:pos + k_mer_length])
    
    # Convert set to list
    k_mers = list(k_mers)
    
    return k_mers
        