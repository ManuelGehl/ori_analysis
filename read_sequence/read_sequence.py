import os

def read_sequence(input_path: str) -> str:
        """
        Reads a sequence from the specified input file in FASTA formate or plain text formate.

        Raises:
            FileNotFoundError: If the specified input file does not exist.
            FileNotFoundError: If the specified input file is empty.

        Reads the sequence from the file using the 'read_fasta' function and stores
        the concatenated sequence in the 'raw_sequence' attribute of the class.

        Returns:
            str: DNA sequence string.
        """
        # Check if file exists
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input file not found: {input_path}")
        # Check if file is not empty
        if os.stat(input_path).st_size == 0:
            raise FileNotFoundError(f"Empty file")
        
        # Check if file is FASTA or plain text
        sequence = ""
        with open(input_path) as file:
            for line in file:
                line = line.strip()
                if not line.startswith(">"):
                    line.upper()
                    sequence += line
                    