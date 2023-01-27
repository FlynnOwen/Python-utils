class TestClass:
    # Include type hints -> all arguments must be of type int
    def __init__(self, attribute1: int, attribute2: int, attribute3: int):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        self.attribute3 = attribute3
        self.names = {}

    def __repr__(self):
        # This is invoked when print() is called on this object
        return f"This is the representation of {self.attribute1}"

    def __str__(self):
        # This is invoked when an object of this class is cast to a string (str())
        return f"{self.__class__.__name__} ({self.attribute1}, {self.attribute2}, {self.attribute3})"

    def __add__(self, other):
        # This is invoked when this object is added (using +) to another
        return self.attribute1 + other.attribute1

    def __len__(self):
        return self.attribute1 + self.attribute2 + self.attribute3

    def __call__(self):
        # This is invoked when the class is called as if a function:
        # E.g object = Testclass()
        # object()
        return 'The object has been called!'

    def __setitem__(self, name, mapping):
        # This is a method of treating the class as a dictionary
        # It is invoked when setting an item as if a dictionary
        # E.g object[name] = mapping
        self.names[name] = mapping

    def __getitem__(self, name):
        # This method is invoked when retrieving an object as if the class is a dictionary
        # E.g object[name]
        return self.names[name]

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

    # ....... setitem method .......#
    test_object1['Flynn'] = 'Owen'
    print(test_object1.names['Flynn'])

    # ....... getitem method .......#
    print(test_object1['Flynn'])