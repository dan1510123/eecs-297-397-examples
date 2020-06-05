#!/usr/local/bin/python3

# Can return single values.

def add(a, b):
    return a + b


# Can return multiple values.
# They are returned as a  tuple.
def get_coordinates(a, b, c):
    x = add(a, b)
    y = add(b, c)

    return x, y             # Or, return (x, y)


# A function can return multiple different types.
# Probably not the most readable/usable code though...
# Just because you *can* do it does not mean it is
# a good idea.
def different_return_types(i):
    if i < 10:
        return i
    else:
        return str(i)



print(add(10, 20))

# Multiple return values are contained in a tuple.
# Can assign the result to multiple variables to
# extract the tuple's values.

x, y = get_coordinates(5, 6, 10)
print(x, y, sep=', ')

# Or get the tuple itself
coordinates = get_coordinates(4, 7, 10)
print(coordinates)


print(type(different_return_types(5)))
print(type(different_return_types(20)))
