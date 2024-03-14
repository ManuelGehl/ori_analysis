from functions.hamming_distance import hamming_distance

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
 
def approximate_pattern_frequency(sequence: str, pattern_length: int, threshold: int) -> dict:
    """
    Determines the frequency of patterns in a DNA sequence within a given Hamming distance threshold.
    Pattern occurences are also count for similar (within threshold Hamming distance) but not identical patterns.

    Parameters:
    - sequence (str): The input DNA sequence.
    - pattern_length (int): The length of the patterns to be considered.
    - threshold (int): The Hamming distance threshold for pattern matching.

    Returns:
    - dict: A dictionary where keys are patterns and values are their frequencies in the sequence.
    """
    # Initialize frequency dictionary
    frequency_dict = {}
    
    # Define scanning range
    scanning_range = len(sequence) - pattern_length + 1

    # Slide a window over the sequence
    for pos in range(scanning_range):
        # Extract the current window
        current_window = sequence[pos:pos + pattern_length]
        # Generate d-neighbourhood of current window
        neighbourhood = generate_d_neighbourhood(sequence=current_window, distance=threshold)
        
        # Calculate hamming distance between current_window and every neighbour from the neighbourhood
        for neighbour in neighbourhood:
            hamming_dist = hamming_distance(current_window, neighbour)
            # If Hamming distance is below threshold include neighbour in dictionary
            if hamming_dist <= threshold:
                # If current_window not in dictionary, initialize with key = 0
                frequency_dict.setdefault(neighbour, 0)
                # If neighbour occured, increase by 1
                frequency_dict[neighbour] += 1

    return frequency_dict

def most_frequent_patterns(frequency_dict: dict) -> list:
    """
    Finds the most frequent patterns in a dictionary of pattern frequencies.

    Parameters:
    - frequency_dict (dict): A dictionary where keys are patterns and values are their frequencies.

    Returns:
    - list: A list containing the most frequent patterns.
    """
    # Determine maximum occurence in dictionary
    max_value = max(frequency_dict.values())
    patterns = []
    # Loop trough dictionary and add most frequent patterns to list
    for pattern, frequency in frequency_dict.items():
        if frequency == max_value:
            patterns.append(pattern)
    
    return patterns

def reverse_complement(sequence: str) -> str:
    """
    Generates the reverse complement of a DNA sequence.

    Parameters:
    - sequence (str): The input DNA sequence.

    Returns:
    - str: The reverse complement of the input sequence.
    """
    # Return sequence
    sequence = sequence[::-1]
    
    # Define mapping dictionary
    mapping_dict = {"A": "T",
                    "T": "A",
                    "G": "C",
                    "C": "G"}
    # Map characters in sequence
    complement_seq = [mapping_dict[char] for char in sequence]
    
    return "".join(complement_seq)

def frequency_merge(frequency_dict_1: dict, frequency_dict_2: dict) -> dict:
    """
    Merges two dictionaries of pattern frequencies.

    Parameters:
    - frequency_dict_1 (dict): The first dictionary of pattern frequencies.
    - frequency_dict_2 (dict): The second dictionary of pattern frequencies.

    Returns:
    - dict: A dictionary containing the merged pattern frequencies.
    """
    # Initialzie empty dictionary
    merged_frequencies = {}
    # Loop trough the union of patterns
    for pattern in set(frequency_dict_1) | set(frequency_dict_2):
        # If the pattern exists in both dictionaries, calculate sum
        # If the pattern exists in only one dictionary, keep orinal count
        merged_frequencies[pattern] = frequency_dict_1.get(pattern, 0) + frequency_dict_2.get(pattern, 0)
    
    return merged_frequencies
    
    
sequence = "ATTATATGC"
distance = 3
neigh = generate_d_neighbourhood(sequence, distance)
for elem in neigh:
    print(elem)
#rev_comp = reverse_complement(sequence)
#freq1 = approximate_pattern_frequency(sequence, 7, 3)
#freq2 = approximate_pattern_frequency(rev_comp, 7, 3)
#merged = frequency_merge(freq1, freq2)
#patts = most_frequent_patterns(frequency_dict=merged)
#print(patts)



