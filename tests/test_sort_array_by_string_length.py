from src.sort_array_by_string_length import sort_by_length

def test_small_array():
    input_array = ["Telescopes", "Glasses", "Eyes", "Monocles"]
    expected_output = ["Eyes", "Glasses", "Monocles", "Telescopes"]
    assert sort_by_length(input_array) == expected_output

def test_medium_array():
    input_array = ["Apple", "Banana", "Orange", "Grape", "Pineapple"]
    expected_output = ["Apple", "Grape", "Banana", "Orange", "Pineapple"]
    assert sort_by_length(input_array) == expected_output

def test_large_arrat():
    input_array = ["Elephant", "Lion", "Tiger", "Giraffe", "Hippopotamus", "Rhinoceros", "Kangaroo", "Crocodile"]
    expected_output = ["Lion", "Tiger", "Giraffe", "Elephant", "Kangaroo", "Crocodile", "Rhinoceros", "Hippopotamus"]
    assert sort_by_length(input_array) == expected_output

