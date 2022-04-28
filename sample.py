import functools


def my_new_decorator(just_a_func):
    @functools.wraps(just_a_func)  # preserving __name__ and __doc__
    def wrapper_my_new_decorator(*args):
        print('Extra code before calling just_a_func()')
        result = just_a_func(*args)
        print('Extra code after calling just_a_func()')
        return result

    return wrapper_my_new_decorator


@my_new_decorator
def just_a_func(x):
    """
    This is the docstring of just_a_func.
    """
    print(f'I\'m just a function. x = {x}')
    return x * x


result = just_a_func(100)
print(f'Returned value result: {result}')

print(f'Function\'s name: {just_a_func.__name__}')
print(f'{just_a_func.__doc__}')