print("Globals to start:", globals(), end="\n\n")

try:
    print(sys.argv)
except NameError:
    print("Did not find sys in any namespace.", end="\n\n")

import sys

# Note that sys now shows up in globals.
print("Globals after import includes sys:", globals(), end="\n\n")


# Once imported sys.argv can be found without error
print(sys.argv)


# Can also import modules or parts of modules with an aliased name
import collections as cols
from sys import argv as command_line_args

print("More globals:", globals(), end="\n\n")



# Can import your own modules too
from my_module import print_hello, print_goodbye


print("Globals with functions from my_module:", globals(), end="\n\n")

print_hello()
print_goodbye()