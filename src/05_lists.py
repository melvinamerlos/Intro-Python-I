# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE

# x.append(y) will give you --> [1, 2, 3, 4, [8, 9, 10]]
x.extend(y) # [1, 2, 3, 4, 8, 9, 10]
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE

x.remove(8) # del x[5] & x.pop(i) --> deletes/pops a specific index
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE

x.insert(5, 99) # first parameter is index loc, followed by valued added
print(x)

# Print the length of list x
# YOUR CODE HERE

print("The length is", len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE

for elements in x:
    print(elements*1000)