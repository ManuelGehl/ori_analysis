from functions.hamming_distance import hamming_distance
from functions.neighbourhood import generate_d_neighbourhood

def pattern_frequency(sequence: str, pattern_length: int, neighbourhood_dict: dict) -> dict:
    """
    Determines the frequency of patterns in a DNA sequence based on their presence in a neighborhood dictionary.

    Parameters:
        sequence (str): The input DNA sequence.
        pattern_length (int): The length of the patterns to be considered.
        neighbourhood_dict (dict): A dictionary containing k-mers as keys and their corresponding d-neighbourhoods as values.

    Returns:
        dict: A dictionary where keys are patterns and values are their frequencies in the sequence.
    """
    # Initialize frequency dictionary
    frequency_dict = {}
    
    # Define scanning range
    scanning_range = len(sequence) - pattern_length + 1

    # Slide a window over the sequence
    for pos in range(scanning_range):
        # Extract the current window
        current_window = sequence[pos:pos + pattern_length]
        # Add 1 to each k_mer which has current_window in d-neighbourhood
        for k_mer, neighbourhood in neighbourhood_dict.items():
            if current_window in neighbourhood:
                frequency_dict.setdefault(k_mer, 0)
                # If neighbour occured, increase by 1
                frequency_dict[current_window] += 1

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

#rev_comp = reverse_complement(sequence)
#freq1 = approximate_pattern_frequency(sequence, 7, 3)
#freq2 = approximate_pattern_frequency(rev_comp, 7, 3)
#merged = frequency_merge(freq1, freq2)
#patts = most_frequent_patterns(frequency_dict=merged)
#print(patts)



