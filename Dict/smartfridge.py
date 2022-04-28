import copy

from contents import recipes, pantry


def add_shopping_item(data: dict, item: str, quantities: int) -> None:
    # if data is list we use below one.But prob is it will produce the result as ('oil', 9)
    # ('l', 8)
    # ('oil', 1) . So oil is present two times
    # data.append((item, quantities))

    # if data is dict this is first way
    # if item not in data:
    #     data[item] = quantities
    # else:
    #     data[item] += quantities

    # if data is dict this is first way
    data[item] = data.setdefault(item, 0) + quantities


shopping_list = {}

print(recipes)

print("Please choose ur recipe")
print("_" * 25);
i = 0;
# first way to produce o/p 1 - ButterChicken
for key in recipes.keys():
    i += 1;
    print(f'{i}  - {key}')
# second way to produce o/p 1 - ButterChicken
for index, key in enumerate(recipes):
    print(f'{index + 1}  - {key}')
# third way to produce o/p 1 - ButterChicken
display_dict = {str(index + 1): key for index, key in enumerate(recipes)}
choice = None
food = "Non-veg"
while choice != '0':
    print("Please choose ur recipe")
    print("_" * 25);
    for index, key in enumerate(recipes):
        print(f'{index + 1}  - {key}')
    choice = input('>')
    if choice in display_dict:
        ingredients = recipes[display_dict[choice]]
        for food_item, required in ingredients.items():
            quantity = pantry.get(food_item, 0)
            if required <= quantity:
                print(f'{food_item} is available')
                pantry[food_item] = quantity - required
                ingredients[food_item] = 0
                print(pantry)
            else:
                quantity_to_buy = required - quantity
                ingredients[food_item] = quantity_to_buy
                pantry[food_item] = 0
                add_shopping_item(shopping_list, food_item, quantity_to_buy)
                print(f'you need to buy a {quantity_to_buy} of {food_item} ')
        key_copys = list(ingredients.keys())

        for key in list(key_copys):
            if ingredients[key] == 0:
                ingredients.pop(key)
        print(ingredients)
    # else:
    #     print("Please choose right option : ")
    # for index, key in enumerate(recipes):
    #     print(f'{index + 1}  - {key}')

for item, value in shopping_list.items():
    print(item, value)
