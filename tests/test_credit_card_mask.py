from src.credit_card_mask import maskify

def test_empty_string():
    assert maskify("") == ""

def test_short_length():
    assert maskify("123") == "123"

def test_long_length():
    assert maskify("4556364607935616") == "############5616"
    assert maskify("64607935616") == "#######5616"
    assert maskify("1") == "1"
    assert maskify("Skippy") == "##ippy"
    assert maskify("Nananananananananananananananana Batman!") == "####################################man!"
