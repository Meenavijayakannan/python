# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}

# Text string
text = "Later in the course, you'll see how to use the collections Counter class."

listval = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
text = text.lower();
print(text)
# Your code goes here ...
for char in text.casefold():
    # We're only counting letters and digits (no punctuation).
    if char.isalnum():
        word_count[char] = word_count.setdefault(char, 0) + 1

# for i in listval:
#     counts = text.count(i);
#     if counts != 0:
#         word_count.setdefault(i, counts)

# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)
