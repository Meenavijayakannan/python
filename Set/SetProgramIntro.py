numbers = set()

# Here i am giving input 12,23,24,12.Set will again ask for a one more input because i entered duplicate value .
# So it shows please enter the number for five times
while len(numbers) < 4:
    next_value = int(input("Please enter the number : "))
    numbers.add(next_value)

# O/P
# Please enter the number : 12
# Please enter the number : 23
# Please enter the number : 24
# Please enter the number : 12
# Please enter the number : 34


# Set wont preserve any order.It gives o/p in a random order and removes duplicates and gives unique data
data = ['blue', 'red', 'red', 'white', 'green', 'red']
unique = set(data)
print(unique)  # {'red', 'blue', 'white', 'green'}

# if we want the data in alphabetical order then we use sorted() but it produces a list
print(sorted(unique))  # ['blue', 'green', 'red', 'white']

# if in the case i want the order of data inserted needs to be
# preserved and at the same time i want unique data use below method
# data = ['blue', 'red', 'red', 'white', 'green', 'red']
# here blue is the first,then red,then white then green where dict.fromkeys(data) produces dict
# and convert to list to et keys alone from dict
unique_data = list(dict.fromkeys(data))
print(unique_data)  # ['blue', 'red', 'white', 'green']
