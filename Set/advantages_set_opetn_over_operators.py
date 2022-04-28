farm = [
    {"hen", "cat", "dog"},
    {"lion", "cat"},
    {"lion", "tiger", "elephant"},
    {"horse", "cock"}
]

allanimals = set()
# first way
allanimals.update(farm[0],
                  farm[1],
                  farm[2],
                  farm[3])

print(sorted(allanimals))  # ['cat', 'cock', 'dog', 'elephant', 'hen', 'horse', 'lion', 'tiger']

# secondway
allanimals_1 = set()
allanimals_1.update(*farm)
print(sorted(allanimals_1))  # ['cat', 'cock', 'dog', 'elephant', 'hen', 'horse', 'lion', 'tiger']

print()
# to get o/p in each line
print(*sorted(allanimals_1), sep='\n')
# o/P
# cat
# cock
# dog
# elephant
# hen
# horse
# lion
# tiger
