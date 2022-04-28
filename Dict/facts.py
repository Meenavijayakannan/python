new = {1: 'one',
       2: 'Two',
       3: 'Three',
       4: 'Four'}
new[5] = 'five'

list_new = new
print(list_new)
list_old = []
new[6] = 'six'
print(list_new)
# for i in new.keys():
#     list_old.append(i)

# Instead of new.keys() we can also use new alone. it will give the same results
for i in new:
    list_old.append(i)
print(list_old)

new_dict = dict(zip('one', 'Two'))
print(new_dict)
# it created dict keys from list and values are none
print(dict.fromkeys(list_old))
# it created dict keys from list and values are 0
print(dict.fromkeys(list_old, 0))
# it returns key and value
print(dict.popitem(new_dict))
# it returns value
print(new_dict.pop('n'))

new = {1: 'one',
       2: 'Two',
       3: 'Three',
       4: 'Four'}
new[5] = 'five'

# update
val = {'4': 4, 5: 5, 6: 6}
new_dict.update(val)  # O/P{'o': 'T', '4': 4, 5: 5, 6: 6}
print(new_dict)

# update will add the values to dict if the keys not exist otherwise it replace the dict values
# O/p {'o': 'T', '4': 4, 5: 5, 6: 6, 0: 1, 1: 2, 2: 3, 3: 4, 4: 5}
new_dict.update(enumerate(new))
print(new_dict)

pantry = ['chicken', 'nuggets', 'owl']
new_dict.update(enumerate(pantry))  # {'o': 'T', '4': 4, 5: 5, 6: 6, 0: 'chicken', 1: 'nuggets', 2: 'owl', 3: 4, 4: 5}
print(new_dict)

# getting values
val = new_dict.values()
print(val)
print('chicken' in val) #prints true
print('cds' in val) #prints false


#One way of finding key using value in a list from dict {'o': 'T', '4': 4, 5: 5, 6: 6, 0: 'chicken', 1: 'nuggets', 2: 'owl', 3: 4, 4: 5}
keys = list(new_dict.keys())
val  = list(new_dict.values())
if 'chicken' in val:
    index = val.index('chicken')
    key = keys[index]
    print(f'{new_dict[key]} found using {key}') # chicken found using 0

#second way
for key,value in new_dict.items():
    if 'chicken' == value:
        print(f'{new_dict[key]} found using {key}') #chicken found using 0

