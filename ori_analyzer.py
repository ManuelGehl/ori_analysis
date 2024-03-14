from functions.sequence import read_sequence
from functions.gc_skew import calculate_gc_skew, plot_skew, min_max_skew
from functions.generate_k_mers import generate_k_mers
from functions.pattern_frequency import reverse_complement, approximate_pattern_frequency, frequency_merge, most_frequent_patterns

class OriAnalyzer():
    
    def __init__(self):
        pass
    
    def read_sequence(self, input_path: str) -> str:
        """
        Reads a DNA sequence from the specified input file using the read_sequence function.

        Args:
            input_path (str): Path to the input file containing the DNA sequence.

        Returns:
            str: DNA sequence string.
        """
        return read_sequence(input_path=input_path)
    
    def calculate_gc_skew(self, sequence: str):
        """
        Calculate GC skew scores for each position in the sequence.

        Parameters:
        - sequence (str): DNA sequence.

        Returns:
        - list: List of GC skew scores.
        """
        return calculate_gc_skew(sequence=sequence)
    
    def plot_skew(self, skew_array: list) -> None:
        """
        Plot GC skew scores as a function of positions in the genome.

        Parameters:
        - skew_array (list): List of GC skew scores.
        """
        plot_skew(skew_array=skew_array)

    def min_max_skew(self, skew_array: list) -> list:
        """
        Calculate minimum and maximum values of GC skew.

        Parameters:
        - skew_array (list): List of GC skew scores.

        Returns:
        - list: Positions where the skew is minimum.
        - list: Positions where the skew is maximum.
        """
        return min_max_skew(skew_array=skew_array)
    
    def generate_k_mers(self, sequence: str, k_mer_length: int, seq_range: tuple = (0, 10)) -> list:
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
        return generate_k_mers(sequence=sequence, k_mer_length=k_mer_length, seq_range=seq_range)
    
    def reverse_complement(self, sequence: str) -> str:
        """
        Generates the reverse complement of a DNA sequence.

        Parameters:
        - sequence (str): The input DNA sequence.

        Returns:
        - str: The reverse complement of the input sequence.
        """
        return reverse_complement(sequence=sequence)
    
    def pattern_frequency(self, sequence: str, pattern_length: int, threshold: int) -> dict:
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
        return approximate_pattern_frequency(sequence=sequence, pattern_length=pattern_length, threshold=threshold)
    
    def most_frequent_patterns(self, frequency_dict: dict) -> list:
        """
        Finds the most frequent patterns in a dictionary of pattern frequencies.

        Parameters:
        - frequency_dict (dict): A dictionary where keys are patterns and values are their frequencies.

        Returns:
        - list: A list containing the most frequent patterns.
        """
        return most_frequent_patterns(frequency_dict=frequency_dict)

    def frequency_merge(self, frequency_dict_1: dict, frequency_dict_2: dict) -> dict:
        """
        Merges two dictionaries of pattern frequencies.

        Parameters:
        - frequency_dict_1 (dict): The first dictionary of pattern frequencies.
        - frequency_dict_2 (dict): The second dictionary of pattern frequencies.

        Returns:
        - dict: A dictionary containing the merged pattern frequencies.
        """
        return frequency_merge(frequency_dict_1=frequency_dict_1, frequency_dict_2=frequency_dict_2)