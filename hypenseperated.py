string_str = "green-red-yellow-black-white";
word_list = string_str.split("-");
word_list.sort();
print("-".join(word_list));