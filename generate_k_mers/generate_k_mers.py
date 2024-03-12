def generate_k_mers(sequence: str, k_mer_length: int, range: tuple = (0, 100)) -> list:
    
    # Define part of sequence to generate k-mers from
    start, stop = range
    sequence_part = sequence[start:stop + 1]
    
    # Define scanning range
    scanning_range = len(sequence_part) - k_mer_length + 1
    
    k_mer_list = []
    # Slide a window over the sequence part
    for pos in range(scanning_range):
        # Add current k-mer to list
        k_mer_list.append(sequence[pos:pos + k_mer_length])
    
    # Remove duplicates
    k_mer_list = list(set(k_mer_list))
    
    return k_mer_list
        