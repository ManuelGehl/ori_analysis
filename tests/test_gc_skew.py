import pytest
from ori_analyzer import OriAnalyzer

# Create fixture for instantiating
@pytest.fixture
def ori_analyzer():
    return OriAnalyzer()

# Test for correct GC skew
def test_gc_skew_correct(ori_analyzer):
    ori_analyzer.genome = "AAAAATTTTTGGGGGCCCCC"
    ori_analyzer.calculate_gc_skew()
    assert ori_analyzer.skew_array == 11 * [0] + [1, 2, 3, 4, 5] + [4, 3, 2, 1, 0]

# Test for handling empty sequence
def test_gc_skew_empty_sequence(ori_analyzer):
    ori_analyzer.genome = ""
    with pytest.raises(ValueError):
        ori_analyzer.calculate_gc_skew()

# Test for handling no sequence
def test_gc_skew_no_sequence(ori_analyzer):
    ori_analyzer.genome = None
    with pytest.raises(ValueError):
        ori_analyzer.calculate_gc_skew()

# Test for handling sequences without purines
def test_gc_skew_no_purines(ori_analyzer):
    ori_analyzer.genome = "ATATATATATATATAT"
    ori_analyzer.calculate_gc_skew()
    assert ori_analyzer.skew_array == len(ori_analyzer.genome) * [0] + [0]

# Test for no skew array
def test_plot_skew_no_array(ori_analyzer):
    ori_analyzer.skew_array = None
    with pytest.raises(ValueError):
        ori_analyzer.plot_skew()

# Test for empty skew array
def test_plot_skew_empty_array(ori_analyzer):
    ori_analyzer.skew_array = []
    with pytest.raises(ValueError):
        ori_analyzer.plot_skew()

# Test for other exceptions
def test_plot_skew(ori_analyzer):
    ori_analyzer.skew_array = [0, 1, 0, 1, 0, 1, 0]
    try:
        ori_analyzer.plot_skew()
    except Exception as e:
        pytest.fail(f"Plotting failed with exception: {e}")

# Test for min max skew
def test_min_max_skew_known_array(ori_analyzer):
    ori_analyzer.skew_array = [0, 1, 0, 1, 0, 1, 0]
    expected_min_positions = [0, 2, 4, 6]
    expected_max_positions = [1, 3, 5]
    assert ori_analyzer.min_max_skew() == (expected_min_positions, expected_max_positions)

# Test for single element
def test_min_max_skew_single_element(ori_analyzer):
    ori_analyzer.skew_array = [0]
    expected_min_positions = [0]
    expected_max_positions = [0]
    assert ori_analyzer.min_max_skew() == (expected_min_positions, expected_max_positions)

# Test for all identical values
def test_min_max_skew_all_identical(ori_analyzer):
    ori_analyzer.skew_array = [1, 1, 1, 1]
    expected_min_positions = [0, 1, 2, 3]
    expected_max_positions = [0, 1, 2, 3]
    assert ori_analyzer.min_max_skew() == (expected_min_positions, expected_max_positions)

# Test for no skew array
def test_min_max_skew_no_array(ori_analyzer):
    ori_analyzer.skew_array = None
    with pytest.raises(ValueError):
        ori_analyzer.plot_skew()

# Test for empty skew array
def test_min_max_skew_empty_array(ori_analyzer):
    ori_analyzer.skew_array = []
    with pytest.raises(ValueError):
        ori_analyzer.plot_skew()