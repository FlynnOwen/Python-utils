list_ = [1, 2, 3, 4, 5, 6, 7, 8]

print('Using range(len())')
for i in range(len(list_)):
    val = list_[i]
    print(i, val)

print('Using enumerate()')
for i, j in enumerate(list_):
    print(i ,j)
