num_list = list()
for i in range(1500,3201):
    if i%7 == 0 and i%5 != 0 :
        num_list.append(str(i));


print(",".join(num_list));