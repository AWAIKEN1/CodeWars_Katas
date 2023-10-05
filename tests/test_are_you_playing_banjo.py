from src.are_you_playing_banjo import are_you_playing_banjo

def test_are_you_playing_banjo():
    assert are_you_playing_banjo("Robert") == "Robert plays banjo"
    assert are_you_playing_banjo("Alice") == "Alice does not play banjo"
    assert are_you_playing_banjo("Rebecca") == "Rebecca plays banjo"
    assert are_you_playing_banjo("rachel") == "rachel plays banjo"
    assert are_you_playing_banjo("Randy") == "Randy plays banjo"
    assert are_you_playing_banjo("Xavier") == "Xavier does not play banjo"
