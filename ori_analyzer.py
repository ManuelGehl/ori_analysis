from sequence import read_sequence

class OriAnalyzer():
    
    def __init__(self):
        pass
    
    def read_sequence(self, input_path):
        """
        Reads a DNA sequence from the specified input file using the read_sequence function.

        Args:
            input_path (str): Path to the input file containing the DNA sequence.

        Returns:
            str: DNA sequence string.
        """
        return read_sequence(input_path=input_path)