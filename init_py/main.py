# Don't need an __init__ file to use import x from y
from non_init_folder import double

print(double.double_number(2))


# By including the importing of classes/functions from scripts in __init__ file, we can save the extra step
import full_init_folder
print(full_init_folder.quadriple_number(2))

# It's possible to define functions in the __init__ file
import init_folder
print(init_folder.triple_number(2))