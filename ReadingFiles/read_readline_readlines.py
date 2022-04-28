# first way using readline
with open('rose.txt') as rose:
    while True:
        line = rose.readline().rstrip()
        print(line)
        if 'Robert Burns' in line:
            break
print("*" * 80)
# second way using for . If we use we cant see robert burns in result. this is a diffrence with readline
with open('rose.txt') as rose:
    for line in rose:
        line = rose.readline().rstrip()
        print(line)
        if 'Robert Burns' in line:
            break

# readlines gives list.If the file size fits into memory use readline
with open('rose.txt') as rose:
    lines = rose.readlines()
    print(lines)  # O/P will be list along with \n

# read give string format of lines.So we dont need to bother about memory
with open('rose.txt') as rose:
    lines = rose.read().rstrip()
    print(lines)
    for line in reversed(lines):
        print(line, end='')
print("-" * 80)
# If we use 'with' keyword while opening, there is no need to close it manually. So there is no chance to forget it.
# If we dont use with keyword then we need to close it manually
rose = open('rose.txt', 'r')

lines = rose.read()
print(lines)

rose.close()  # if we forget to close , it will lead to a file handling problems

print()
# How to remove the specific characters or symbols from the line
with open('rose.txt') as rose:
    lines = rose.readline().rstrip()
print(lines) # O my Luve's like a red, red rose
# give a characters and symbols that needs to be removed
chars = "rose"
removed = lines.strip(chars)
print(removed) # O my Luve's like a red, red


#remove suffix and prefix
with open('rose.txt') as rose:
    lines = rose.readline().rstrip()
prefix_removed = lines.removeprefix("O my").lstrip()
print(prefix_removed)

suffix_removed = lines.removesuffix("rose")
print(suffix_removed)
