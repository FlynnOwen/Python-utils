# Use a context manager when opening files

# Open the file in write (w) mode
f = open('file1.txt', 'w')

# Write 'hello' to the file
f.write('hello')

# Close (save) the file
f.close()

# Using a context manager (with automatically closes the file when the context manager exits)
with open('file2.txt', 'w') as f:
    f.write('hello')
