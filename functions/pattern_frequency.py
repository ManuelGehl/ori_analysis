def pattern_frequency(sequence: str, seq_range: tuple, neighbourhood_dict: dict) -> dict:
    """
    Determines the frequency of patterns in a DNA sequence based on their presence in a neighborhood dictionary.

    Parameters:
        sequence (str): The input DNA sequence.
        neighbourhood_dict (dict): A dictionary containing k-mers as keys and their corresponding d-neighbourhoods as values.

    Returns:
        dict: A dictionary where keys are patterns and values are their frequencies in the sequence.
    """
    
    # Check for correct data types
    if not isinstance(sequence, str) or not isinstance(seq_range, tuple) or not isinstance(neighbourhood_dict, dict):
        raise ValueError("Input sequence as string, seq_range as tuple and neighbourhood_dict as dictionary.")
    # Check that no input is empty
    if len(sequence) == 0:
        raise ValueError("Empty sequence.")
    if len(seq_range) == 0:
        raise ValueError("Empty sequence range.")
    if len(neighbourhood_dict) == 0:
        raise ValueError("Empty neighbourhood dictionary.")
    
    # Initialize frequency dictionary
    frequency_dict = {}
    # Extract pattern length from neighbourhood dictionary
    pattern_length = len(next(iter(neighbourhood_dict.keys())))
    # Define part of sequence to generate k-mers from
    start, stop = seq_range
    
    # Check sequence range values
    if not 0 <= start < len(sequence) or not 0 <= stop < len(sequence) or not start < stop:
        raise ValueError("Invalid sequence range. Please provide a valid range within the length of the sequence.")
    
    # Define slice of sequence from which k-mers will be generated
    sequence_part = sequence[start:stop + 1]
    
    # Define scanning range
    scanning_range = len(sequence_part) - pattern_length + 1

    # Slide a window over the sequence
    for pos in range(scanning_range):
        # Extract the current window
        current_window = sequence_part[pos:pos + pattern_length]
        # Add 1 to each k_mer which has current_window in d-neighbourhood
        for k_mer, neighbourhood in neighbourhood_dict.items():
            if current_window in neighbourhood:
                frequency_dict.setdefault(k_mer, 0)
                # If neighbour occured, increase by 1
                frequency_dict[k_mer] += 1

    return frequency_dict

def most_frequent_patterns(frequency_dict: dict) -> tuple:
    """
    Finds the most frequent patterns in a dictionary of pattern frequencies.

    Parameters:
    - frequency_dict (dict): A dictionary where keys are patterns and values are their frequencies.

    Returns:
    - tuple: Number of occurences, a list containing the most frequent patterns.
    """
    
    # Check for correct data types
    if not isinstance(frequency_dict, dict):
        raise ValueError("Input frequency_dict as dictionary.")
    # Check that no input is empty
    if len(frequency_dict) == 0:
        raise ValueError("Empty neighbourhood dictionary.")
    
    # Determine maximum occurence in dictionary
    max_value = max(frequency_dict.values())
    patterns = []
    # Loop trough dictionary and add most frequent patterns to list
    for pattern, frequency in frequency_dict.items():
        if frequency == max_value:
            patterns.append(pattern)
    
    return max_value, patterns