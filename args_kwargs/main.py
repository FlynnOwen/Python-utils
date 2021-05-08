def my_arg_func(*args):
    print(args)
    print(*args)


def my_kwarg_func(**kwargs):
    print(kwargs)
    print(list(kwargs.items()))
    print(list(kwargs.values()))
    print(list(kwargs.keys()))


if __name__ == '__main__':
    my_arg_func(1, 2, 3)
    my_kwarg_func(first='1', second='3', third='5')

