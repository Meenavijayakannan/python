import copy

from deepcopy_challenge import deepcopy

original = {
    "Tim" : ["Buchalka",["Programmer","teacher"]],
    "J-P" : ["Roberts",["Programmer","teacher"]]
}

original_copy = {}

copy1 = copy.deepcopy(original)
copy2 = deepcopy(original,original_copy)

original["Tim"].append("Australia")
original["J-P"].append("UK")
original["Tim"][1].append("Cashier")
original["J-P"][1].append("Courier")

print(original)
print(copy1)
print(copy2)