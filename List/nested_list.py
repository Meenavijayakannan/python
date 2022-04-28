menu = [
    ["egg", "sauce"],
    ["tomato", "sauce", "egg"],
    ["egg", "sauce", "spam"],
    ["egg", "spam"],
    ["sauce", "spam"],
    ["tomato", "spam"],
    ["egg", "spam"],
    ["egg", "spam", "veg", "tomato", "bascon"],
    ["egg"]
]
for food in menu:
    if "spam" not in food:
        print("Meal has good items {}", food)

for meal in menu:
    for index in range(len(meal) - 1, -1, -1):
        if meal[index] == "spam":
            del meal[index];
    print(meal)

for meal in menu:
    for item in meal:
        if item != "spam":
            print(item)
    print()

numbers = input("please enter three numbers")
list_num = numbers.split(",")
int_list = list()
value =0
for index in list_num :
    int_list.append(int(index))

a,b,c=int_list
value = a+b-c
print(value)
