# We get a set containing all the integers from zero to 20, inclusive.
# The values appear in order, but don't be fooled! Sets have no ordering.
# Python has to print them out in some order, and will sometimes display a set of integers in order.
# But don't think that means the set is ordered – it isn't.
# This is an effect of the way sets are implemented, in CPython.
# If you're using a different implementation of Python, you may get different output
numbers = set(range(21))
print(numbers)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

# remove which will throw exception if the data is not exist
numbers.remove(9)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
# numbers.remove(99) won't allow to execute anything because it will throw exception.So use try except
try:
    numbers.remove(99)
    print(numbers)
except KeyError:
    print("Number not exist")  # O/P Number not exist when we use try except

# O/P if there is no try except
# Traceback (most recent call last):
#  File "D:\Users\mguruvappan\PycharmProjects\pythonProject\python\Set\removing_items.py", line 12, in <module>
#    numbers.remove(99)
# KeyError: 99

# If we dont want any code crash, then use discard because it dont care
# whether element exist or not.If exist it will remove otherwise other work will happen
numbers.discard(10)
numbers.discard(100)
print(numbers)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

# Pop will remove and return the element.It is same as list
# and dict but it is not indexable, so we cant pass arguments
element = numbers.pop() # the first element is popped
print(element) #O/P : 0
