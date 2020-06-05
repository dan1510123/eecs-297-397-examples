#!/usr/local/bin/python3

# Tuples group together elements like lists, but tuples are immutable

numbers = (1, 2, 3, 4)
print(numbers)

# Cannot modify elements. The next line would result in an error.
# numbers[2] = 10



# If tuples contain mutable objects, the mutable object can change.

first_and_last_names = ([], [])
first_and_last_names[0].append("Matt")
first_and_last_names[1].append("Sargent")

print(first_and_last_names)

