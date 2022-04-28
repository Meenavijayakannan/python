string_str = "I love cat and dogs"
words = string_str.split(" ");
i=0
for w in words :
    words[i]=w[::-1];
    i+=1;
print(" ".join(words))


