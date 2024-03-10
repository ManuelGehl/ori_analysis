from hamming_distance import hamming_distance

def generate_direct_neighbours(sequence: str) -> list:
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
    # Determine maximum occurence in dictionary
    max_value = max(frequency_dict.values())
    patterns = []
    # Loop trough dictionary and add most frequent patterns to list
    for pattern, frequency in frequency_dict.items():
        if frequency == max_value:
            patterns.append(pattern)
    
    return patterns

def reverse_complement(sequence: str) -> str:
    # Return sequence
    sequence = sequence[::-1]
    
    # Define mapping dictionary
    mapping_dict = {"A": "T",
                    "T": "A",
                    "G": "C",
                    "C": "G"}
    # Define empy list
    complement_seq = []
        
    # Map characters in sequence
    for char in sequence:
        complement_seq.append(mapping_dict[char])
    
    return "".join(complement_seq)

def frequency_merge(frequency_dict_1: dict, frequency_dict_2: dict) -> dict:
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



