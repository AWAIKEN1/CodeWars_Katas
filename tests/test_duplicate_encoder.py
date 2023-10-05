from src.duplicate_encoder import duplicate_encode

def test_duplicate_encode_single_occurrence():
    assert duplicate_encode("din") == "((("
    assert duplicate_encode("a") == "("
    assert duplicate_encode("1234") == "(((("

