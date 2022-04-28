def sum_numbers(*args: float) -> float:
    """
    This is used to calculate the sum of the given numbers
    :param args: accepts float,int
    :return: returns float
    """
    return sum(args)


print(sum_numbers(1, 2, 3))
print(sum_numbers(12.5, 3.147,98.1))
print(sum_numbers(8, 20, 2))
print(sum_numbers(1.1, 2.2, 5.5))