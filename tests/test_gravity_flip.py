from src.gravity_flip import flip

def test_flip_with_direction_R():
    assert flip("R", [3,2,1,2]) == [1,2,2,3]
    assert flip("R", [1,4,5,3,2,1,3]) ==[1,1,2,3,3,4,5]
    assert flip("R", [5,4,3,2,1]) == [1,2,3,4,5]

def test_flip_with_direction_L():
    assert flip("L", [1,2,3,4,5]) == [5,4,3,2,1]
    assert flip("L", [1, 4, 5, 3, 5]) == [5, 5, 4, 3, 1]
    assert flip("L", [1,4,5,3,2,1,3]) == [5,4,3,3,2,1,1]

def test_flip_with_empty_list():
    assert flip("R", []) == []
    assert flip("L", []) == []

def test_flip_with_single_element():
    assert flip("R", [5]) == [5]
    assert flip("L", [5]) == [5]
