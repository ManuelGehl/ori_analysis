from ori_analyzer import OriAnalyzer

def main():
    """
    The main function of the OriC pipeline.

    Reads the genome sequence ("genome.txt"), calculates GC skew, generates 9-mers, and finds the most frequent patterns
    within a specified sequence range. Prints the results.
    """
    analyzer = OriAnalyzer()
    # Read genome sequence and calculate skew values
    analyzer.read_sequence("genome.txt")
    analyzer.calculate_gc_skew()
    min_position, max_position = analyzer.min_max_skew()
    print(f"Positions with minimum skew values: {min_position}")
    print(f"Positions with maximum skew values: {max_position}")
    # Get user input
    k_mer_length = 9
    start_pos = min_position[0]
    stop_pos = start_pos + 500
    
    # Generate k-mers and neighbourhood
    k_mers = analyzer.generate_k_mers(k_mer_length=k_mer_length,
                                      seq_range=(start_pos, stop_pos))
    neighbourhood = analyzer.neighbourhood_dictionary(k_mers=k_mers,
                                                      distance=1,
                                                      reverse_complement=True)
    # Generate pattern frequency
    frequency = analyzer.pattern_frequency(seq_range=(start_pos, stop_pos),
                                           neighbourhood_dict=neighbourhood)
    max_value, patterns = analyzer.most_frequent_patterns(frequency_dict=frequency)
    # Output patterns
    print(f"The following {k_mer_length}-mers have been found {max_value} times in the given sequence range")
    for pattern in patterns:
        print(pattern)

if __name__ == "__main__":
    main()