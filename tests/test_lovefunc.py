from src.lovefunc import lovefunc

def test_flower_one_even_and_flower_two_odd():
    assert lovefunc(4, 5) == True

def test_flower_one_odd_and_flower_two_even():
    assert lovefunc(4, 5) == True

def test_both_have_even_petals():
    assert lovefunc(8, 8) == False

def test_both_have_even_petals():
    assert lovefunc(5, 5) == False

def test_for_large_amount_of_petals():
    assert lovefunc(60, 63) == True
    assert lovefunc(45, 60) == True
    assert lovefunc(100, 100) == False
    assert lovefunc(111, 111) == False
