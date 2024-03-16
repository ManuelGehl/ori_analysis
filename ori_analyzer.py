from functions.sequence import read_sequence as read_seq_func, reverse_complement
from functions.gc_skew import calculate_gc_skew as gc_skew_func, plot_skew as plot_skew_func, min_max_skew as min_max_skew_func
from functions.generate_k_mers import generate_k_mers as generate_k_mers_func
from functions.pattern_frequency import pattern_frequency as pattern_freq_func
from functions.pattern_frequency import frequency_merge as merge_func, most_frequent_patterns as most_frequent_func
from functions.neighbourhood import neighbourhood_dictionary as neighbourhood_func

class OriAnalyzer():
    
    def __init__(self):
        self.genome = None
        self.skew_array = None
        self.frequency_dict = None
    
    def read_sequence(self, input_path: str) -> None:
        """
        Reads a DNA sequence from the specified input file using the read_sequence function.

        Args:
            input_path (str): Path to the input file containing the DNA sequence.

        Returns:
            str: DNA sequence string.
        """
        self.genome = read_seq_func(input_path=input_path)
    
    def calculate_gc_skew(self) -> None:
        """
        Calculate GC skew scores for each position in the sequence.

        Parameters:
        - sequence (str): DNA sequence.

        Returns:
        - list: List of GC skew scores.
        """
        self.skew_array = gc_skew_func(sequence=self.genome)
    
    def plot_skew(self) -> None:
        """
        Plot GC skew scores as a function of positions in the genome.

        Parameters:
        - skew_array (list): List of GC skew scores.
        """
        plot_skew_func(skew_array=self.skew_array)

    def min_max_skew(self) -> list:
        """
        Calculate minimum and maximum values of GC skew.

        Parameters:
        - skew_array (list): List of GC skew scores.

        Returns:
        - list: Positions where the skew is minimum.
        - list: Positions where the skew is maximum.
        """
        return min_max_skew_func(skew_array=self.skew_array)
    
    def generate_k_mers(self, k_mer_length: int, seq_range: tuple = (0, 10)) -> list:
        """
        Generate unique k-mers from a specified range of the genomic DNA sequence.

        Parameters:
        - sequence (str): The input DNA sequence.
        - k_mer_length (int): Length of k-mers to generate.
        - seq_range (tuple, optional): A tuple representing the range of the sequence to consider.
                                        Default is (0, 10).

        Returns:
        - list: List of unique k-mers.
        """
        return generate_k_mers_func(sequence=self.genome, k_mer_length=k_mer_length, seq_range=seq_range)
    
    def neighbourhood_dictionary(self, k_mers: list, distance: int, reverse_complement: bool = False) -> dict:
        """
        Generates a dictionary of k-mers and their corresponding d-neighbourhoods.

        This method takes a list of k-mers and generates a dictionary where each k-mer is paired with its d-neighbourhood,
        defined as the set of all k-mers that can be formed by changing at most 'distance' positions in the original k-mer.

        Parameters:
        - k_mers (list): A list of k-mers (strings).
        - distance (int): The maximum Hamming distance for generating d-neighbourhoods.
        - reverse_complement (bool, optional): Flag indicating whether to include reverse complements of k-mers in the
        neighbourhoods. Defaults to False.

        Returns:
        - dict: A dictionary where keys are k-mers and values are lists of k-mers representing their d-neighbourhoods.
        If reverse_complement is True, each k-mer's value also includes its d-neighbourhoods' reverse complements.

        Example:
        Given k_mers = ['ACGT', 'ATGC'] and distance = 1:
        neighbourhood_dictionary(k_mers, distance) returns {'ACGT': ['ACGT', 'ACTT', 'AGGT', 'ACCT', 'ACGG'],
                                                            'ATGC': ['ATGC', 'AGGC', 'AAGC', 'ATCC', 'TTGC']}
        """
        neighbourhood = neighbourhood_func(k_mers=k_mers, distance=distance)
        
        if reverse_complement:
            # Initialize empty neighbourhood dictionary
            neighbourhood_rev_comp = {}
            # Iterate over all neighbourhood lists and add the reverse_complement sequences to each
            for k_mer, neighbours in neighbourhood.items():
                rev_comp = [reverse_complement(neighbour) for neighbour in neighbours]
                neighbourhood_rev_comp[k_mer] = list(set(neighbours + rev_comp))
            return neighbourhood_rev_comp
        
        else:
            return neighbourhood
                    
    def pattern_frequency(self, seq_range: tuple, neighbourhood_dict: dict) -> dict:
        """
        Determines the frequency of patterns in a DNA sequence based on their presence in a neighborhood dictionary.

        Parameters:
            sequence (str): The input DNA sequence.
            neighbourhood_dict (dict): A dictionary containing k-mers as keys and their corresponding d-neighbourhoods as values.

        Returns:
            dict: A dictionary where keys are patterns and values are their frequencies in the sequence.
        """
        return pattern_freq_func(sequence=self.genome, seq_range=seq_range, neighbourhood_dict=neighbourhood_dict)
    
    def most_frequent_patterns(self, frequency_dict: dict) -> list:
        """
        Finds the most frequent patterns in a dictionary of pattern frequencies.

        Parameters:
        - frequency_dict (dict): A dictionary where keys are patterns and values are their frequencies.

        Returns:
        - list: A list containing the most frequent patterns.
        """
        return most_frequent_func(frequency_dict=frequency_dict)