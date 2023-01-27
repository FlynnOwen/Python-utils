def my_arg_func(*args):
    # Args is a tuple
    print(args)
    print(*args)


def my_kwarg_func(**kwargs):
    # Kwargs is loaded in as a dictionary
    print(kwargs)
    print(list(kwargs.items()))
    print(list(kwargs.values()))
    print(list(kwargs.keys()))


def my_func(first, second, third):
    print(first)
    print(second)
    print(third)


if __name__ == '__main__':
    my_arg_func(1, 2, 3)
    my_kwarg_func(first='1', second='3', third='5')

    my_dict = {'first': '1', 'second': '3', 'third': '7'}
    my_func(**my_dict)
    my_func(*(1,2,3))

