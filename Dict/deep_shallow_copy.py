import copy

lion_list = ['lion', 'tiger']
dog_list = ['dog', 'cat']
animals = {
    'wild': lion_list,
    'domestic': dog_list,
}
things = {
    'wild': lion_list,
    'domestic': dog_list,
}
things['domestic'].append('horse')
# Both id of domestic list are same in shallow copy
print(id(things['domestic']))  # 1596688503424
print(id(animals['domestic']))  # 1596688503424

# not only copies references of anumal object like shallow copy but also copies the refernces of list objects deeply
things = copy.deepcopy(animals);
# Both id of domestic list are different in deep copy by using copy module so we imported copy
print(id(things['domestic']))  # 1596693006208
print(id(animals['domestic']))  # 1596688503424
