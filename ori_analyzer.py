from functions.sequence import read_sequence
from functions.gc_skew import calculate_gc_skew, plot_skew, min_max_skew

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