def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(prefix, 'Executed before', original_function.__name__)
            result = original_function(*args, **kwargs)
            print(prefix, 'Executed after', original_function.__name__, '\n')
            return result
        return wrapper_function
    return decorator_function


@prefix_decorator('Prefix!')
def display_info(name, age):
    print(f'display_info ran with arguments ({name}, {age})')


display_info('John', 25)
display_info('Rod', 35)
