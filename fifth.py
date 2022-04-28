sequence = [1, 5, 19, 3, 31, 100, 55,89]
for item in sequence:
    if item % 17 == 0:
        print('A number divisible by 17 has been found! Breaking the loop...')
        break   #breaks out of the loop (executes the first instruction (if any) after the else block of code)
else:
    print('There is no number divisible by 17 in the sequence')