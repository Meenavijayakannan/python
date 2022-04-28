animals = {
    'wild' :  'lion',
    'domestic' : 'dog'
}
#when we assign refernce of animal to things, if any changes carried out in animals will als gets reflect in things
things = animals
animals['both'] = 'horse'
print(things)      #{'wild': 'lion', 'domestic': 'dog', 'both': 'horse'}
print(animals)     #{'wild': 'lion', 'domestic': 'dog', 'both': 'horse'}
#Both ids are same
print(id(things))    #1684755514240
print(id(animals))   #1684755514240

#If we need two different dictionaries then we use shallow copy
things = animals.copy()
animals['both'] = 'cat'
print(things)     #{'wild': 'lion', 'domestic': 'dog', 'both': 'horse'}
print(animals)     #{'wild': 'lion', 'domestic': 'dog', 'both': 'cat'}

#Both ids are diffrent
print(id(things))   #1684755514304
print(id(animals))  #1684755514240


# animals = {
#     'wild' : ['lion','tiger'],
#     'domestic': ['dog','cat'],
# }
lion_list = ['lion','tiger']
dog_list = ['dog','cat']
animals = {
    'wild' : lion_list,
    'domestic': dog_list,
}
things = {
    'wild' : lion_list,
    'domestic': dog_list,
}

#If we need two different dictionaries then we use shallow copy but if the values in dict are list then it wont happen
things = animals.copy()
animals['domestic'].append('pig')
print(things)     #{'wild': ['lion', 'tiger'], 'domestic': ['dog', 'cat', 'pig']}
print(animals)     #{'wild': ['lion', 'tiger'], 'domestic': ['dog', 'cat', 'pig']}

#Both ids are diffrent
print(id(things))   #2364481733568
print(id(animals))  #2364481747648
lion_list.append('leopard')
animals['wild'].append('added via animals')
things['wild'].append('added via things')


print(things)  #{'wild': ['lion', 'tiger', 'leopard', 'added via animals', 'added via things'], 'domestic': ['dog', 'cat', 'pig']}
print(animals) #{'wild': ['lion', 'tiger', 'leopard', 'added via animals', 'added via things'], 'domestic': ['dog', 'cat', 'pig']}
