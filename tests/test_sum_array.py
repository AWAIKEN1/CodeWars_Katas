from src.sum_array import sum_array

def test_with_less_than_3_numbers():
    a = [1,2,3]
    assert sum_array(a) == 6

def test_with_double_digit_numbers():
    a = [10,15,20]
    assert sum_array(a) == 45

def test_with_decimals():
    a = [1.1, 2.2, 3.3]
    assert sum_array(a) == 6.6

def test_with_no_numbers():
    a = []
    assert sum_array(a) == 0


