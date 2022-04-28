def sentence_palindrome(word):
    string = "";
    for char in word:
        if char.isalnum():
            string += char
    print(string)
    answer = palindrome_fn(string)
    return answer


def palindrome_fn(string):
    return string[::-1].casefold() == string.casefold()


variable_check = input("Type the string")
result = sentence_palindrome(variable_check.lower())
if result:
    print("This is a palindrome")
else:
    print("This is a not a palindrome")
