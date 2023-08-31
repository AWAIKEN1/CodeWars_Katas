def remove_trailing_zeros(n):
    num_str = str(n)

    if "." in num_str:
        num_str = num_str.rstrip("0").rstrip(".")
    else:
        num_str = num_str.rstrip("0")

    if num_str == '' or num_str == '.':
        return 0

    if "." not in num_str:
        return int(num_str)

    return float(num_str)