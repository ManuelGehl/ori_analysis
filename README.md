# ori_analyzer

ori_analyzer is a Python package designed for analyzing single DNA sequences and identifying potential origin of replication (ori) regions. This package offers a range of functionalities to facilitate genomic analysis, including calculating GC skew, generating k-mers, determining pattern frequencies, and finding the most frequent patterns.

## Summary of Features:

- **Reading DNA Sequences:** The package provides functionality to read DNA sequences from input files.
- **Calculating GC Skew:** Users can calculate GC skew scores for each position in the sequence, which can be indicative of ori regions.
- **Plotting GC Skew:** Visualize GC skew scores as a function of positions in the genome.
- **Finding Min-Max Skew Positions:** Identify positions where the GC skew is minimum and maximum.
- **Generating k-mers:** Generate unique k-mers from specified ranges of genomic DNA sequences.
- **Generating Neighbourhood Dictionary:** Create a dictionary of k-mers and their corresponding d-neighbourhoods, useful for motif analysis.
- **Determining Pattern Frequency:** Determine the frequency of patterns in a DNA sequence based on their presence in a neighborhood dictionary.
- **Finding Most Frequent Patterns:** Identify the most frequent patterns in a dictionary of pattern frequencies.

## ori_pipeline

The `ori_pipeline` script provides a simple default pipeline for analyzing genome sequences to identify the origin of replication (OriC). It assumes the following prerequisites:

- The genome sequence is stored as a plain text file named "genome.txt".
- The analyzed k-mer length is set to 9, which is the default for *E. coli*.
- The region to analyze extends from the minimum skew position to 500 base pairs downstream.

Usage and output for *E. coli* genome:
```{bash}
>>> python3 ori_pipeline.py

Positions with minimum skew values: [3923620, 3923621, 3923622, 3923623]
Positions with maximum skew values: [1550413]
The following 9-mers have been found 4 times in the given sequence range
AGCTGGGAT
GATCCCAGC
GCTGGGATC
CTGGGATCA
GGATCCTGG
TGTGGATAA
TTATCCACA
GTTATCCAC
GTGGATAAC
```
