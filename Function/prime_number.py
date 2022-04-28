def prime_number(n):
    count = 0
    for i in range(2, n):
        if n % i == 0:
            count += 1
    return count


data = prime_number(9)
if data > 1:
    print("This is not a prime number")
else:
    print("This is a prime number")

list_value = list()
for n in range(1_000_000, 100_000_000):
    data = prime_number(n)
    if data < 1:
        list_value.append(n)
    if len(list_value) == 5:
        print(list_value)
        break;
