nums = '10,20,30,40,50';
num_list = nums.split(",");
int_list = list();
for i in range(len(num_list)):
    int_list.append(int(num_list[i]));

print(int_list);