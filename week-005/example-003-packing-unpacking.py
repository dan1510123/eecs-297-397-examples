# Sometimes you will have a list or dictionary you wish
# to use to call a function, but you do not want to have
# to pull out individual values to pass to a function.
# Unpacking to the rescue!

def addAll(*args):
    return sum(args)

def add2(a, b):
    return addAll(a, b)

def add3(a, b, c):
    return addAll(a, b, c)


# Say you have a list or tuple and you want to call
# one of the functions above.

values = (5, 10)
other_values = [11, 13, 14]

# Passing these variables to the functions directly
# will result in an error:
# add2(values)        # ERROR
# add3(other_values)  # ERROR

# We can use '*' to unpack the values in a list or tuple
# and pass them to functions:

print(add2(*values))
print(add3(*other_values))


# We used * to pack values with functions.
# See addAll(*args) above.

print(addAll(1, 2, 5, 6, 7))


### What is the following code doing?
data = {"a":3, "b":4, "c":5}
print(add3(**data))

add3(a=3, b=4, c=5)




