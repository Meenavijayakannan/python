def fibonacci_series(n, a=0, b=1):
    i = 2
    print(0, a)
    print(1, b)
    while i <= n-1:
        c = a + b
        a = b
        b = c
        i += 1;
        print(i, c)


value = int(input("Enter the value"))
fibonacci_series(value)
