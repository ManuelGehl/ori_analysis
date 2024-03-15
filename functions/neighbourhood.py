def generate_direct_neighbours(sequence: str) -> list:
    """
    Generates direct neighbors of a given DNA sequence.

    Parameters:
    - sequence (str): The input DNA sequence.

    Returns:
    - list: A list containing the input sequence and its direct neighbors.
    
    Example:
    >>> generate_direct_neighbours(sequence="ATG")
    ['ATG', 'TTG', 'GTG', 'CTG', 'AAG', 'AGG', 'ACG', 'ATA', 'ATT', 'ATC']
    """
    nucleotide_list = ["A", "T", "G", "C"]
    # Initialize direct neighbours with sequence
    direct_neighbours = [sequence]
    
    # Loop trough every nucleotide in sequence
    for position, nucleotide in enumerate(sequence):
        # Generate list of possible nucleotides to exchange at each position
        candidate_list = [candidate for candidate in nucleotide_list if candidate != nucleotide]
        for candidate in candidate_list:
            # Split sequence and replace nucleotides
            split_sequence = list(sequence)
            split_sequence[position] = candidate
            # Join sequence to string and append to list
            modified_sequence = ''.join(split_sequence)
            direct_neighbours.append(modified_sequence)
    
    return direct_neighbours

def generate_d_neighbourhood(sequence: str, distance: int) -> list:
    """
    Generates a d-neighborhood of a given DNA sequence.

    Parameters:
    - sequence (str): The input DNA sequence.
    - distance (int): The maximum hamming distance of all neighbours relative to the input sequence.

    Returns:
    - list: A list containing the input sequence and its d-neighbors within the specified distance.
    
    Example:
    >> generate_d_neighbourhood(sequence="AT")
    ['AG', 'CG', 'GA', 'TC', 'GG', 'AA', 'AT', 'GT', 'CT', 'CC', 'AC', 'GC', 'TG', 'CA', 'TA', 'TT']
    """
    # Initialize neighbourhood
    neighbourhood = [sequence]
    if distance == 0:
        return neighbourhood
    
    for _ in range(distance):
        # Initialize temporary storage
        current_neighbours = []
        # Iterrate over sequences in neighbourhood
        for seq in neighbourhood:
            direct_neighbours = generate_direct_neighbours(sequence=seq)
            current_neighbours += direct_neighbours
        
        # Add current neighbours to neighbourhood
        neighbourhood += current_neighbours
        # Remove duplicates
        neighbourhood = list(set(neighbourhood))
    
    return neighbourhood