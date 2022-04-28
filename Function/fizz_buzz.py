def fizz_buzz(n : int) -> str:
    """
    This function is used to return the fizz buzz for the number 15
    :param n: It accepts a integer
    :return: return string
    """
    if n % 15 == 0:
        return "fizz buzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return str(n)


# for i in range(1,101):
#     print(fizz_buzz(i))

input("Press Enter to start")
print()

next_number = 0
while next_number < 99 :
    next_number+=1;
    print(fizz_buzz(next_number))
    next_number+=1
    correct_answer = fizz_buzz(next_number)
    player_answer = input("Enter the value")
    if correct_answer == player_answer :
        print("Well done")
    else :
        print("Wrong")