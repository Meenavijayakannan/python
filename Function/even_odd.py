def sum_eo(n, t):
    """
    This sum_eo function is used to calculate the sum of even and odd numbers
    :param n: n is a range upto odd number to be calculated
    :param t: t is a sting type denotes even or odd
    :return: sum of range
    """
    # summing_value = 0;
    start = None
    if t == 'e':
        start = 2
    elif t == 'o':
        start = 1
    else:
        return -1;
    return sum(range(start, n, 2))


string_type = input("Enter the string")
value = int(input("Enter the range"))
answer = sum_eo(value, string_type)
print(answer)
help(sum_eo)
