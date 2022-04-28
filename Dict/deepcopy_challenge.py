def deepcopy(recipes: dict, recipes_copy: dict) -> dict:
    for k, v in recipes.items():
        newvalue = v.copy()
        recipes_copy[k] = newvalue
        # recipes_copy[k] = {}
        # for ke, va in recipes[k].items():
        #     recipes_copy[k][ke] = va
    return recipes_copy


recipe = {
    "Butter chicken": {"potato": 5, "oil": 10},
    "Chicken and chips": {"k": 6, "l": 8, "oil": 2},
    "Pizza": {"veg": 9, "Non-veg": 10}
}
recipes_copies = {}
recipe_copy = deepcopy(recipe, recipes_copies)
print(recipe_copy)
recipe_copy['Butter chicken']['potato'] = 300
print(recipe_copy['Butter chicken']['potato'])
print(recipe['Butter chicken']['potato'])
