def is_isogram(string):
    word = string.lower()

    letters = []

    for letter in word:
        if letter in letters:
            return False
        else:
            letters.append(letter)

    return True