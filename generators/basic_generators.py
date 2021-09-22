# Generator using yield
def basic_generator(number: int) -> dict:
    for i in range(number):
        yield {i: i + 1}


x = basic_generator(3)

print(next(x))
print(next(x))

print(type(x))

# comprehension_generator
x = ({i: i + 1} for i in range(10))

print(next(x))
print(next(x))

print(type(x))