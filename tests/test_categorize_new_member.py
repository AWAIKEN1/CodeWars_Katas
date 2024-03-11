from src.categorize_new_member import open_or_senior

def test_open_or_senior():
    assert open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]) == ['Open', 'Senior', 'Open', 'Senior']
    assert open_or_senior([(18, 20), (45, 2), (61, 12), (37, 6), (21, 21), (78, 9)]) == ['Open', 'Open', 'Senior', 'Open', 'Open', 'Senior']
    assert open_or_senior([(60, 8), (50, 10), (70, 5)]) == ['Senior', 'Open', 'Open']
