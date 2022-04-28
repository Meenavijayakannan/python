def ctofconverter(celsius):
    fahrenheit = (celsius * (9 / 5)) + 32
    return fahrenheit


def birthday(month, day):
    monthtuple = [('Jan', 31), ('Feb', 28), ('Mar', 31), ('Apr', 30), ('May', 31), ('Jun', 30)]
    totaldays = 0
    for i in range(0, month - 1):
        totaldays += monthtuple[i][1]
    return totaldays + day


print(int(ctofconverter(25)))
import math
from math import *

print(math.cos(23))
print(math.pow(2, 6))
print(2 ** 6)
temp = 'I am learning pandas'
val = temp.split()
print(val[1])

print(temp[2:4])

mylist = [1, 2, 3, [4, 5, ['Hello', True], 23.6], 34]
print(mylist[3][2][0])

mylist.remove(34)
print(mylist)

# monthtuple  = [('Jan',31),('Feb',28)]
# print(monthtuple[1][1])
print(birthday(5, 25))

mydict = {'k1': [2, 25, False], 'k2': {'k3': [1, 'Hello']}}
print(mydict.get('k2').get('k3')[1])
