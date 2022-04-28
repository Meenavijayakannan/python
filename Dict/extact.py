phone = {'Brand': 'Samsung', 'Price': 650.2, 'Seller': 'Nile'}

## YOUR CODE STARTS HERE
# price = phone['Price']
#
# vat = float(price * (19 / 100))
# print(round(vat, 2))

# my_list = [1, 2.3, 'abc', (5, 6, 'x', 'y')]
#
# ## YOUR CODE STARTS HERE
# my_var = str(my_list[1]) + my_list[2][0]+my_list[3][3]
# print(my_var)

# languages = ['English', 'Python', 'Java', 'Golang', 'German']
#
# ## YOUR CODE STARTS HERE
# language = languages[1:4]
# print(language)
#
# days = [10, 11, 13, 14, 15]
#
# ## YOUR CODE STARTS HERE
# # Using a list method insert the value 12 between 11 and 13.
# days.insert(2,12)
# print(days)

# message = 'Wow! Python is great'
# vowels = 'aeio'
#
# no_vowels = list(char for char in message if char not in vowels and char != ' ')
# print(no_vowels)

names1 = {'John', 'Marry', 'Lena', 'Pollux'}
names2 = {'Dan', 'Arthur', 'Marry', 'Lena', 'Castor'}

## Using set methods create a list called names that contains the elements that belong to both sets
## names will be  ['Lena', 'Marry']
## YOUR CODE STARTS HERE
# names = names1.union(names2)
# print(names)
# name = names1 | names2
# print(name)

# my_str  = 'wlo1      Link encap:Ethernet  HWaddr b4:6d:83:77:85:f3'
#
# ## YOUR CODE STARTS HERE
# list_str = my_str.split()
# print(list_str[0]+ '!' +list_str[4])
#
# def myfunction(x):
#     sum_value = 0
#     value_list = list()
#     for i in range(1, 4):
#         value_list.append(x * i)
#     for i in value_list:
#         sum_value += int(i)
#     print(sum_value)
#
#
# myfunction('5')


## List with duplicates
mac = ['b4:6d:83:77:85:f3', 'b4:6d:83:77:85:f3', 'a4:6d:83:77:85:f4', 'c4:6d:83:77:85:f3', 'b4:6d:83:77:85:f3']
mac_unique = list()


# ## YOUR CODE STARTS HERE
# for address in mac:
#     if address not in mac_unique:
#         mac_unique.append(address);
#
# print(mac_unique)
# [mac_unique.append(address) for address in mac if address not in mac_unique]
# print(mac_unique)


# ## List of Words
# words = ['Anna', 'Car', 'Civic', 'Screen', 'Level', 'Cat', 'Mom' ]
#
# ## YOUR CODE STARTS HERE
# palindromes = list()
# # [palindromes.append(w) for w in words if w == w[::-1]]
#
#
# for w in words :
#     if w.lower() == w[::-1].lower():
#         palindromes.append(w)
# print(palindromes)


# def remove_from_list(my_list, item):
#     """
#     Function that removes all accurrances of item from my_list
#     """
#     ## YOUR CODE STARTS HERE
#
#     for i in range(len(my_list)):
#         if item == my_list[len(my_list) -1 -i]:
#             my_list.remove(item)
#
#     return my_list
#
#
# list1 = [1, 2, 1, 1, 3]
# answer = remove_from_list(list1, 1)
# print(answer)


# countries = ['USA', 'UK', 'France', 'Romania', 'France', 'Germany', 'USA', 'Canada', 'India', 'UK']
#
# ## YOUR CODE STARTS HERE
# sorted_list=sorted(list(set(countries)))
# print(sorted_list)

with open('show_arp.txt','r') as file:
    contents = file.read().splitlines()
    contents = contents[1:]
    ip_mac = list()
    for line in contents:
       ip  =  line.split()[1]
       mac =  line.split()[3]
       ip_mac.append((ip,mac))

    print(ip_mac)