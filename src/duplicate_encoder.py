def duplicate_encode(word):
    result = ""
    char_count = {}

    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
        print(char_count)

    for char in word:
        if char_count[char] > 1:
            result += ")"
        else:
            result += "("

    return result

