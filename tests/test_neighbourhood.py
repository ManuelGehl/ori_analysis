import pytest
from ori_analyzer import OriAnalyzer

# Create fixture for instantiating
@pytest.fixture
def ori_analyzer():
    return OriAnalyzer()

# Test for neighbourhood_dictionary
def test_neighbourhood_dictionary(ori_analyzer):
    k_mers = ["ATG", "ATG"]
    distance = 1
    expected_neighbourhood_dict = {
        "ATG": sorted(["ATG", "TTG", "CTG", "GTG", "AAG", "ACG", "AGG", "ATA", "ATC", "ATT"]),
        "ATG": sorted(["ATG", "TTG", "CTG", "GTG", "AAG", "ACG", "AGG", "ATA", "ATC", "ATT"])
        }
    assert ori_analyzer.neighbourhood_dictionary(k_mers, distance) == expected_neighbourhood_dict