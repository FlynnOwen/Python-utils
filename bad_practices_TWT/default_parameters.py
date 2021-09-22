# Using mutable default parameters

def append_number(num, numbers=[]):
    numbers.append(num)

    return numbers


def append_number_immutable(num, nums=()):
    nums += (num,)

    return nums


x = append_number(1)
y = append_number(2)
z = append_number(3)

# Notice that the numbers object is being appended to regardless of it's call
print(x)
print(y)
print(z)

print(x is y and y is z)

x = append_number_immutable(1)
y = append_number_immutable(2)
z = append_number_immutable(3)

print(x)
print(y)
print(z)