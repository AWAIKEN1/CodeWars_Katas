from src.string_to_array import string_to_array

def test_non_empty_string_with_multiple_words():
    input_string = "Robin Singh"
    result = string_to_array(input_string)
    assert result == ["Robin", "Singh"]

def test_non_empty_string_with_a_sentence():
    input_string = "I love arrays they are my favorite"
    result = string_to_array(input_string)
    assert result == ["I", "love", "arrays", "they", "are", "my", "favorite"]

def test_empty_string():
    input_string = ""
    result = string_to_array(input_string)
    assert result == [""]

def test_non_empty_string_with_leading_and_trailing_spaces():
    input_string = "   Spaces   "
    result = string_to_array(input_string)
    assert result == ["Spaces"]

def test_non_empty_string_with_multiple_spaces_between_words():
    input_string = "I  love   spaces"
    result = string_to_array(input_string)
    assert result == ["I", "love", "spaces"]

