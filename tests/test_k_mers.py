import pytest
from ori_analyzer import OriAnalyzer

# Create fixture for instantiating
@pytest.fixture
def ori_analyzer():
    return OriAnalyzer()

# Test for valid input parameters
def test_generate_k_mers_valid_params(ori_analyzer):
    sequence = "ATCGATCGATCG"
    k_mer_length = 3
    seq_range = (0, 6)
    expected_k_mers = sorted(["ATC", "TCG", "CGA", "GAT"])
    ori_analyzer.genome = sequence
    assert ori_analyzer.generate_k_mers(seq_range=seq_range, k_mer_length=k_mer_length) == expected_k_mers

# Test for invalid input types
def test_generate_k_mers_invalid_input_types(ori_analyzer):
    sequence = 123
    seq_range = (0, 6)
    k_mer_length = "3"
    ori_analyzer.genome = sequence
    with pytest.raises(ValueError):
        ori_analyzer.generate_k_mers(k_mer_length=k_mer_length, seq_range=seq_range)

# Test for invalid sequence range
def test_generate_k_mers_invalid_sequence_range(ori_analyzer):
    sequence = "ATCG"
    seq_range = (5, 2)
    k_mer_length = 3
    ori_analyzer.genome = sequence
    with pytest.raises(ValueError):
        ori_analyzer.generate_k_mers(k_mer_length=k_mer_length, seq_range=seq_range)

# Test for invalid k-mer length
def test_generate_k_mers_invalid_kmer_length(ori_analyzer):
    sequence = "ATCG"
    seq_range = (0, 3)
    k_mer_length = 0
    ori_analyzer.genome = sequence
    with pytest.raises(ValueError):
        ori_analyzer.generate_k_mers(k_mer_length=k_mer_length, seq_range=seq_range)