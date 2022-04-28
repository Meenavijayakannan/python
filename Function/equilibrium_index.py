def equilibrium(eq_lists):
    sum_front = 0
    sum_back = 0
    mid = int((len(eq_lists) / 2))
    for i in range(0, mid):
        sum_front += eq_lists[i]
    for i in range(mid + 1, len(eq_lists)):
        sum_back += eq_lists[i]
    return sum_back == sum_front


eq_list = [-7, 1, 5, 2, -4, 3, 0]
answer = equilibrium(eq_list)
if answer:
    print("There is a equilibrium index")
else:
    print("There is not a equilibrium index")
