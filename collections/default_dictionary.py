from _collections import defaultdict

# When creating a default dict object - specify a default value
d1 = defaultdict(dict)

# Dictionary is empty after initialising
print(d1)

# Trying to return a value that doesn't exist instead returns the default value
print(d1[1])

# The error value has been added to the dict
print(d1)


# Define a callable to be the default return value
def test_value():

    return {'one'  : 1,
            'two'  : 2,
            'three': 3}


d2 = defaultdict(test_value)
print(d2)
print(d2[1])
print(d2)

'''
Inner workings:
defaultdict calls __getitem__ to retrieve an item. If it isn't present, it calls __missing__
'''

print(d2.__missing__(2))
print(d2.__getitem__(3))