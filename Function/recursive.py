def factorial(n: int) -> int:
    """
    Factorial is used to calculate the multiple representation of the numbers
    :param n: accepts int
    :return: returns int
    """
    if n <= 1:
        return 1;
    return n * factorial(n - 1)


for i in range(0, 36):
    print(i, factorial(i))
