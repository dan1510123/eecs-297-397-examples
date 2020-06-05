#!/usr/local/bin/python3

numbers = list(range(10))     # values 0 - 9

print(numbers)

# Can slice a list to operate on a part of it.
# Syntax is similar to range.

first_three = numbers[0:3]
print(first_three)

# Omit first argument, still starts at index 0
first_three = numbers[:3]
print(first_three)


# Can slice from the middle of a list too.

print(numbers[4:7])


# Omit last argument, goes to end of list.
print(numbers[8:])


# With no arguments, makes a copy of the list
new_list = numbers[:]

print(new_list)

numbers.append(100)

print(numbers)
print(new_list)            # Only numbers gets the new entry
