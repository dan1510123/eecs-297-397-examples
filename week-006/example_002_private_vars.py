class GuitarString:
    def __init__(self, material, note):
        self.material = material
        self.note = note


# Python does not have "real" private variables or
# methods. Instance variables can be accessed with
# using __dict__

e_string = GuitarString("nylon", "E")
print(e_string.__dict__)

# I can modify these variables at will.
e_string.material = "wood"
print(e_string.__dict__)


# There are conventions for "private" variables in Python.
# Neither of these make a variable truly private, but they
# can signal to others to be treated as such.
#
# If you see variables with underscores in front, do not
# access them outside the class.
class FakePrivateVariableDemo:
    def __init__(self, arg1, arg2):
        self._non_public_thing = arg1  # Single underscore signals non-public part of class.
        self.__mangled_thing = arg2    # 2+ underscores and the variable name will be "mangled"
                                       # in the class dictionary -> _ClassName__variable_name

    def print_mangled(self):
        print(self.__mangled_thing)

demo = FakePrivateVariableDemo(123, 456)

# Modify "private" variable.
# DO NOT ACTUALLY DO THIS EVER.
demo.__dict__["_FakePrivateVariableDemo__mangled_thing"] = "OHNO!!!"

print(demo.__dict__)

# Can still access the "private" variables.
# It is just more of a pain to do so and is bad coding practice.
print(demo.__dict__['_non_public_thing'])
print(demo._non_public_thing)
print(demo.__dict__['_FakePrivateVariableDemo__mangled_thing'])
print(demo._FakePrivateVariableDemo__mangled_thing)

# The following line would result in an error though:
# print(demo.__mangled_thing)
