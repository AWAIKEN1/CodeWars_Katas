from src.even_or_odd import even_or_odd

def test_even_number():
    result = even_or_odd(4)
    assert result == "Even"

def test_odd_number():
    result = even_or_odd(9)
    assert result == "Odd"

def test_zero():
    result = even_or_odd(0)
    assert result == "Even"

def test_negative_even_number():
    result = even_or_odd(-10)
    assert result == "Even"

def test_negative_odd_number():
    result = even_or_odd(-15)
    assert result == "Odd"