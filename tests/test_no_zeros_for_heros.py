from src.no_zeros_for_heros import remove_trailing_zeros

def test_remove_trailing_zeros():
    assert remove_trailing_zeros(1450) == 145
    assert remove_trailing_zeros(960000) == 96
    assert remove_trailing_zeros(1050) == 105
    assert remove_trailing_zeros(-1050) == -105

def test_with_no_trailing_zeros():
    assert remove_trailing_zeros(12345) == 12345
    assert remove_trailing_zeros(42) == 42
    assert remove_trailing_zeros(-7) == -7

def test_cases_with_only_trailing_zeros():
    assert remove_trailing_zeros(0) == 0
    assert remove_trailing_zeros(100000) == 1
    assert remove_trailing_zeros(-70000) == -7

§§