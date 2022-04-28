string_str = "I love cat and dogs"
words = string_str.split(" ");

words = [w[::-1]for w in words]
   
print(" ".join(words))