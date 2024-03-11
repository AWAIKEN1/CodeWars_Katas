def open_or_senior(data):
    categories = []
    for tuple_element in data:
        age = tuple_element[0]
        handicap = tuple_element[1]

        if age >= 55 and handicap > 7:
            categories.append("Senior")
        else:
            categories.append("Open")

    return categories