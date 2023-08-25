from src.stringy_strings import stringy

def test_stringy_even_size():
    assert stringy(6) == '101010'

def test_stringy_smallest_even_size():
    assert stringy(2) == '10'

def test_stringy_odd_size():
    assert stringy(5) == '10101'

def test_stringy_smallest_odd_size():
    assert stringy(1) == '1'

def test_stringy_larger_even_size():
    assert stringy(10) == '1010101010'

def test_stringy_larger_odd_size():
    assert stringy(11) == '10101010101'

def test_stringy_edge_case_size_0():
    assert stringy(0) == ''