farm = {"hen", "cat", "dog"}
wild = {"lion", "tiger", "elephant"}

# Set is commutative.so it gives the element in same order like 2*4 = 4*2 , 1+2 = 2+1
allanimals_1 = farm.union(wild)
print(allanimals_1)  # {'elephant', 'dog', 'tiger', 'cat', 'lion', 'hen'}

allanimals_2 = wild.union(farm)
print(allanimals_2)  # {'elephant', 'dog', 'tiger', 'cat', 'lion', 'hen'}

allanimals_3 = wild | farm
print(allanimals_3)  # {'elephant', 'dog', 'tiger', 'cat', 'lion', 'hen'}

print(wild)  # {'lion', 'elephant', 'tiger'}
wild.update(farm)
print(wild)  # {'lion', 'elephant', 'tiger', 'dog', 'hen', 'cat'}

print(farm)  # {'dog', 'hen', 'cat'}
farm |= wild
print(farm)  # {'dog', 'hen', 'cat', 'lion', 'elephant', 'tiger'}

