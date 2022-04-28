def palindrome(name):
    return name[::-1]


variable_check = input("Type the string")
result = palindrome(variable_check.lower())
if variable_check.lower() == result:
    print("This is a palindrome")
else:
    print("This is a not a palindrome")
