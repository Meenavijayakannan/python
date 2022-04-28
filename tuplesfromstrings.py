list_str =  ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
tuple_list = tuple()
i=0
# for w in list_str:
#     list_str[i] =(w,len(w));
#     i+=1;

list_str= [(w,len(w)) for w in list_str]
print(list_str)