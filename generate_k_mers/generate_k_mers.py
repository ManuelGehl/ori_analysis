def generate_k_mers(sequence: str, k_mer_length: int, seq_range: tuple = (0, 10)) -> list:
    """
    Generate unique k-mers from a specified range of a DNA sequence.

    Parameters:
    - sequence (str): The input DNA sequence.
    - k_mer_length (int): Length of k-mers to generate.
    - seq_range (tuple, optional): A tuple representing the range of the sequence to consider.
                                    Default is (0, 10).

    Returns:
    - list: List of unique k-mers.
    """
    # Validate input parameters
    if not isinstance(sequence, str) or not isinstance(k_mer_length, int) or not isinstance(seq_range, tuple):
        raise ValueError("Invalid input types. Please provide a valid DNA sequence, integer k-mer length, and a tuple for seq_range.")
    
    # Define part of sequence to generate k-mers from
    start, stop = seq_range
    
    # Check sequence range values
    if not 0 <= start < len(sequence) or not 0 <= stop < len(sequence) or not start < stop:
        raise ValueError("Invalid sequence range. Please provide a valid range within the length of the sequence.")
    
    # Define slice of sequence from which k-mers will be generated
    sequence_part = sequence[start:stop + 1]
    
    # Check k_mer_length value
    if not 0 < k_mer_length <= len(sequence_part):
        raise ValueError("Invalid k-mer length. Please provide a positive integer less than or equal to the length of the sequence part.")
    
    # Define scanning range
    scanning_range = len(sequence_part) - k_mer_length + 1
    
    k_mer_set = set()
    # Slide a window over the sequence part
    for pos in range(scanning_range):
        # Add current k-mer to set
        k_mer_set.add(sequence_part[pos:pos + k_mer_length])
    
    # Convert set to list
    k_mer_list = list(k_mer_set)
    
    return k_mer_list
        