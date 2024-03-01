from src.isogram import is_isogram

def test_short_isogram():
    assert is_isogram("abcd") == True
    assert is_isogram("abdfg") == True

def test_long_isogram():
    assert is_isogram("abcdefghijklmnopqrstuvwxyz") == True

def test_short_is_not_isogram():
    assert is_isogram("aabbcc") == False

def test_long_is_not_isogram():
    assert is_isogram("aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == False

