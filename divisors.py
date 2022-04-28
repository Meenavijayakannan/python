number = int(input("Enter the number"));
divisors =list()
for i in range(2,number-1):
    if number%i == 0 :
        divisors.append(i);
        print(i);

if len(divisors) > 0:
    print("{} is not an prime number".format(number));
else :
    print("{} is an prime number".format(number));

