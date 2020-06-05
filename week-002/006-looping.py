#!/usr/local/bin/python3

squares = [x ** 2 for x in range(1, 10)]     # Will cover this syntax soon!

print(squares)


# Can loop through a sequence with a for loop.
# for variable in thing_to_iterate_over:
#     Indented lines of code are in the loop.
#     Can have multiple lines to do things.
#     All indented lines have access to current value of variable.
#
# Once lines are no longer indented, they are outside the for loop.

for square in squares:
    print(square, end = ', ')
print(square ** 0.5)


# Can also loop over characters in a string

for c in "This is a string":
    print(c, end = ' ')
print()


# Can loop using index as well

for i in range(len(squares)):
    print(squares[i], end = ' ')
print()
