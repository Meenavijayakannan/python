def factorial(n):
    value = 1
    if n <= 1:
        return 1;
    while n > 1:
        value *= n
        n = n - 1
    return value


for i in range(0, 36):
    print(i, factorial(i))
