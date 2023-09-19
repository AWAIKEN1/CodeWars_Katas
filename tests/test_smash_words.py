from src.smash_words import smash

def test_smash_words_basic():
    word_array = ['hello', 'world', 'this', 'is', 'great']
    result = smash(word_array)
    assert result == 'hello world this is great'

