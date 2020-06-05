#!/usr/local/bin/python3

def print_name(first, last, middle=''):
    print(first, end=' ')
    if middle != '':
        print(f"{middle[:1].capitalize()}.", end=' ')
    print(last)

# Positional arguments must match the order in
# the function definition.

print_name("Thomas", "Stevens", "James")



# Keyword arguments can be given in any order.
#
# PEP 8 Style:
#
#     Don't use spaces around the = sign when used to
#     indicate a keyword argument, or when used to indicate
#     a default value for an unannotated function parameter.

print_name(first="Thomas", middle="James", last="Stevens")
print_name(last="Stevens", first="Thomas", middle="James")
print_name(first="Thomas", last="Stevens", middle="James")

# Other orderings would be valid too.






# Default values:
# Function definitions can include default values for parameters.
# If no argument is provided for a given parameter, then the
# default value will be used.
# 
# !!!! Note !!!!
# Non-default arguments cannot follow default arguments in 
# a function definition. See below for error example.
# See help(print) for valid example.
# 
# >>> def broken(a=' ', b):
# ...     return
# ... 
#   File "<stdin>", line 1
# SyntaxError: non-default argument follows default argument

print_name("Thomas", "Stevens")
print_name(first="Thomas", last="Stevens")

# These are equivalent to print_name("Thomas", "Stevens", "")














