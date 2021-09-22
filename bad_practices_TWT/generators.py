# iter and next methods make up an iterator

# Generator by tuple comprehension
x = (i*2 for i in range(10))

print(list(x))

# Generator by map
x = map(lambda x:x*2, range(10))

print(list(x))

# Building an iterator class:
class Iterator:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.current = -1

        return self

    def __next__(self):
        self.current += 1

        if self.current >= self.n:
            raise StopIteration

        return self.current


x = Iterator(5)
for i in x:
    print(i)


# Creating a generator
def gen(n):
    for i in range(n):
        yield i


for i in gen(5):
    print(i)


# yield 'pauses' the function execution
def test_gen():
    yield 1

    print('This is a pause!')
    yield 2


x = test_gen()
print(next(x))
print(next(x))
# This will raise StopIteration error
print(next(x))

