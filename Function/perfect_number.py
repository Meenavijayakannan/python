def perfect_number(n):
    perfect = 0
    for i in range(1, n - 1):
        if n % i == 0:
            perfect += i

    return n == perfect;


result = perfect_number(9)
if result:
    print("This is a perfect number")
else :
    print("This is not a perfect number")