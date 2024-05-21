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
    
    # Check that sequence is not empty or none
    if sequence is None or len(sequence) == 0:
        raise ValueError("Empty sequence")
    # Check for correct data type
    if not isinstance(sequence, str):
        raise ValueError("Invalid input type. Please provide a valid sequence.")
    
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
    
    return sorted(direct_neighbours)

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
    
    # Check that sequence is not empty or none
    if sequence is None or len(sequence) == 0:
        raise ValueError("Empty sequence")
    # Check for correct data type
    if not isinstance(sequence, str) or not isinstance(distance, int):
        raise ValueError("Invalid input types. Please provide a valid sequence or distance.")
    # Check for non-negative distances
    if distance < 0:
        raise ValueError("Negative distance.")
    
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
    
    return sorted(neighbourhood)

def neighbourhood_dictionary(k_mers: list, distance: int) -> dict:
    """
    Generates a dictionary of k-mers and their corresponding d-neighbourhoods.
    
    Parameters:
    
    - k_mers (list): A list of k-mers.
    - distance (int): The maximum Hamming distance for generating d-neighbourhoods.

    Returns:
    
    - dict: A dictionary where keys are k-mers and values are their d-neighbourhoods.
    """
    # Check that k_mers is not empty or none
    if k_mers is None or len(k_mers) == 0:
        raise ValueError("Empty k_mers")
    # Check for correct data type
    if not isinstance(k_mers, list) or not isinstance(distance, int):
        raise ValueError("Invalid input types. Please provide a valid list of k-mers or distance.")
    # Check for non-negative distances
    if distance < 0:
        raise ValueError("Negative distance.")
    
    # Initialize empty neighbourhood dictionary
    neighbourhood_dict = {}
    # Iterate over all k-mers, use them as keys and generate the corresponding d-neighbourhood
    for k_mer in k_mers:
        neighbourhood_dict[k_mer] = generate_d_neighbourhood(sequence=k_mer, distance=distance)
        
    return neighbourhood_dict