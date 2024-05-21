import matplotlib.pyplot as plt
import seaborn as sns 

def calculate_gc_skew(sequence: str) -> list:
    """
    Calculate GC skew scores for each position in the sequence.

    Parameters:
    - sequence (str): DNA sequence.

    Returns:
    - list: List of GC skew scores.
    """
    
    # Check that sequence is not empty or none
    if sequence is None or len(sequence) == 0:
        raise ValueError("Empty sequence")
    # Check for correct data type
    if not isinstance(sequence, str):
        raise ValueError("Invalid input type. Please provide a valid sequence.")
    
    # Initialize skew skew_array with 0
    skew_array = [0]
    
    # Iterate over sequence and add scores if Cytosine or Guanine appear
    for pos, nucleotide in enumerate(sequence):
        if nucleotide == "C":
            current_sum = skew_array[pos] - 1
        elif nucleotide == "G":
            current_sum = skew_array[pos] + 1
        else:
            current_sum = skew_array[pos] + 0

        # Append current valute to array
        skew_array.append(current_sum)
        
    return skew_array

def plot_skew(skew_array: list) -> None:
    """
    Plot GC skew scores as a function of positions in the genome.

    Parameters:
    - skew_array (list): List of GC skew scores.
    """
    
    # Check that skew array is not empty or none
    if skew_array is None or len(skew_array) == 0:
        raise ValueError("Empty skew_array")
    # Check for data type
    if not isinstance(skew_array, list):
        raise ValueError("Invalid input type. Please provide a valid skew_array.")
    
    # Plot GC skew as function of positions in genome
    sns.set_style("ticks")
    plt.xlabel("Position")
    plt.ylabel("GC Skew Score")
    plt.title("GC Skew Analysis")
    plt.plot(skew_array)
    plt.show()

def min_max_skew(skew_array: list) -> list:
    """
    Calculate minimum and maximum values of GC skew.

    Parameters:
    - skew_array (list): List of GC skew scores.

    Returns:
    - list: Positions where the skew is minimum.
    - list: Positions where the skew is maximum.
    """
    # Check that skew array is not empty or none
    if skew_array is None or len(skew_array) == 0:
        raise ValueError("Empty skew_array")
    # Check for data type
    if not isinstance(skew_array, list):
        raise ValueError("Invalid input type. Please provide a valid skew_array.")
    
    # Calculate minimum and maximum values of GC skew
    minimum_skew = min(skew_array)
    maximum_skew = max(skew_array)
    
    # Determines all positions where the skew is minimum and maximum
    minimum_positions = [index for index, skew in enumerate(skew_array) if skew == minimum_skew]
    maximum_positions = [index for index, skew in enumerate(skew_array) if skew == maximum_skew]
    
    return minimum_positions, maximum_positions