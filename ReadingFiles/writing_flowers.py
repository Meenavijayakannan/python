import sys

# Saving the reference of the standard output
original_stdout = sys.stdout
data = [
    "Aster-shrub",
    "Azalea-shrub",
    "Black-Eyed Susan-shrub",
    "Buttercup- shrub",
    "California Poppy-shrub",
    "Chrysanthemum-shrub",
    "Crocus-shrub",
    "Daffodil-shrub"
]
# print function allows to write the string representation of object and includes newline and space by default
with open("flowers.txt", "w") as flowers:
    sys.stdout = flowers
    for flower in data:
        print(flower)
    sys.stdout = original_stdout

new_list = []
with open("flowers.txt") as flowers:
    for flower in flowers:
        new_list.append(flower.rstrip())

print(new_list)

# write function expects string representation and do not include space and newline. We have to give it explicitly
with open("flower.txt", "w") as flowers:
    for flower in data:
        flowers.write(flower + "\n")

#TypeError: write() argument must be str, not int
with open("number.txt", "w") as flowers:
    for i in range(0,51):
        #flowers.write(i) # gives TypeError: write() argument must be str, not int
        flowers.write(str(i)+"\n")

with open("number.txt", "a") as flowers:
    for i in range(51,56):
        #flowers.write(i) # gives TypeError: write() argument must be str, not int
        flowers.write(str(i)+"\n")