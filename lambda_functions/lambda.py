# lambda arguments : expression

add_ten = lambda a : a + 10
mult = lambda a, b : a * b

if __name__ == '__main__':
    print(add_ten)
    print(add_ten(5))

    print(mult(2, 5))