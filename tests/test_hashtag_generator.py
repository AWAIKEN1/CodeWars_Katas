from src.hashtag_generator import generate_hashtag


def test_valid_hashtag():
    assert generate_hashtag("hello world") == "#HelloWorld"
    assert generate_hashtag("python is great") == "#PythonIsGreat"


def test_empty_string():
    assert generate_hashtag("") is False


def test_long_string():
    long_string = "a" * 200
    assert generate_hashtag(long_string) is False
