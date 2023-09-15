def abbrev_name(name):
    words = name.split()

    first_initial = words[0][0].upper()
    second_initial = words[1][0].upper()

    return f"{first_initial}.{second_initial}"


# Could also do with tuple unpakcing
# def name_to_initials(name):
#   first, last = name.split()
#   return f"{first[0].upper()}.{last[0].upper()}"
