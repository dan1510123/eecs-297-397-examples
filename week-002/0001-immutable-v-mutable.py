#!/usr/local/bin/python3

# the id() function returns the identity of an object.
# Often location in memory, but not a requirement.

a = 5
b = a

# Variables reference the same place in memory.
print("a and b have the same id: ", id(a), id(b))


a += 10

# Even though we "modify" a, the variable acutally
# points to a new object. The ids of a and b are 
# no longer equal.
print("a and b no longer have the same id: ", id(a), id(b), end = "\n\n")

# The behavior above is because ints are immutable
# in Python. Floats and strings (str) are as well.


# Lists (we will see these soon) are mutable. 
# Their state can change while the underlying object
# remains the same.

c = [1, 2, 3]
d = c

print("c and d have the same id: ", id(c), id(d))
print(c, d, sep = "\n")

# Changing the state of the underlying list will not
# change the id of the underlying object.

c.remove(1)

print("c and d still have the same id: ", id(c), id(d))
print(c, d, sep = "\n")
