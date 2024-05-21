import pytest
from ori_analyzer import OriAnalyzer

# Create fixture for instantiating
@pytest.fixture
def ori_analyzer():
    return OriAnalyzer()

# Test for correct initialization
def test_initialization(ori_analyzer):
    assert ori_analyzer.genome is None
    assert ori_analyzer.skew_array is None