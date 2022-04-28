user = {'username': 'jo', 'level': 'admin'}


def user_has_permission(func):
    def wrapper_ha_per():
        if user['level'] == 'admin':
            return func()
        else:
            return None

    return wrapper_ha_per()


def show():
    return "success"


my_function = user_has_permission(show)
print(my_function)
