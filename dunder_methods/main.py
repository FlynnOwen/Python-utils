class TestClass:
    # Include type hints -> all arguments must be of type int
    def __init__(self, attribute1: int, attribute2: int, attribute3: int):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        self.attribute3 = attribute3

    def __repr__(self):
        return f"This is the representation of {self.attribute1}"

    def __str__(self):
        return f"{self.__class__.__name__} ({self.attribute1}, {self.attribute2}, {self.attribute3})"

    def __add__(self, other):
        return self.attribute1 + other.attribute1

    def __len__(self):
        return self.attribute1 + self.attribute2 + self.attribute3

    def __call__(self):
        return 'The object has been called!'


if __name__ == '__main__':
    test_object1 = TestClass(1, 2, 3)
    print(test_object1)
    print(str(test_object1))
    print(repr(test_object1))

    #...... Same with using dunder representation .......#
    print('\n')
    print(test_object1.__str__())
    print(test_object1.__repr__())

    #....... add method .......#
    test_object2 = TestClass(4, 5, 6)
    print(test_object1 + test_object2)

    # ....... len method .......#
    print(len(test_object1))

    # ....... call method .......#
    print(test_object1())
