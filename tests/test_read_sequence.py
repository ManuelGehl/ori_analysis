import pytest
from pathlib import Path
from ori_analyzer import OriAnalyzer

# Create fixture for instantiating
@pytest.fixture
def ori_analyzer():
    return OriAnalyzer()

# Test for correct reading of file
def test_read_sequence_plain(ori_analyzer):
    # Prepare test file
    test_path = Path("tests/test_sequence.txt")
    with open(test_path, "w") as file:
        file.write("AAAAATTTTTGGGGGCCCCC")
    
    # Test for correct reading
    ori_analyzer.read_sequence(input_path=test_path)
    assert ori_analyzer.genome == "AAAAATTTTTGGGGGCCCCC"

# Test for non-existing file
def test_read_sequence_file_not_found(ori_analyzer):
    with pytest.raises(FileNotFoundError):
        ori_analyzer.read_sequence(input_path=Path("no_file.txt"))

# Test for empty file
def test_read_sequence_empty_file(ori_analyzer):
    # Prepare test file
    test_path = Path("tests/test_sequence.txt")
    with open(test_path, "w") as file:
        file.write("")
    
    with pytest.raises(FileNotFoundError):
        ori_analyzer.read_sequence(input_path=test_path)
        
# Test for correct reading of FASTA
def test_read_sequence_fasta(ori_analyzer):
    # Prepare test file
    test_path = Path("tests/test_sequence.txt")
    with open(test_path, "w") as file:
        file.write(">Header\nAAAAA\nTTTTT\nGGGGG\nCCCCC")
    
    # Test for correct reading
    ori_analyzer.read_sequence(input_path=test_path)
    assert ori_analyzer.genome == "AAAAATTTTTGGGGGCCCCC"

# Test for correct reading of file with lowercase characters
def test_read_sequence_lowercase(ori_analyzer):
    # Prepare test file
    test_path = Path("tests/test_sequence.txt")
    with open(test_path, "w") as file:
        file.write(">Header\naaaaa\nTTTTT\nggggg\nCCCCC")
    
    # Test for correct reading
    ori_analyzer.read_sequence(input_path=test_path)
    assert ori_analyzer.genome == "AAAAATTTTTGGGGGCCCCC"

