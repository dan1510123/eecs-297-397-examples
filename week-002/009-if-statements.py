#!/usr/local/bin/python3

# if statements use indentation to create blocks of code.
# Syntax:
#    if conditional_statement:
#        indented code for the if block
#

a = 7

if a < 10:
    print("This is inside the if block")
    print("So is this")

    if a == 5:
        print("This is part of the inner if block")

    print("Last line in the if")

print("This line is outside the if block")



# Also have elif and else blocks when multiple conditions
# need to be checked in a particular order.

b, c = 10, 20

if b > c:
    print("b is greater than c")
elif c > b:
    print("c is greater than b")
else:
    print("b is equal to c")





# Combine logic with and/or

if a < b and b < c:
    print("a, b, and c are in order!")


if b > a or b > c:
    print("b is not the lowest value.")
