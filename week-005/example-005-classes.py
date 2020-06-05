# Class that does nothing.
class EmptyClass:
    pass

# Class with one instance variable.
class SingleArgClass:
    def __init__(self, arg1):
        self.arg_one = arg1

# Class with two instance variables
# and a single class variable.
class TwoArgClass:
    a_class_var = "Shared by all instances"

    def __init__(self, arg1, arg2):
        self.arg_one = arg1
        self.arg_two = arg2

# Can instantiate classes using () with the correct
# number of arguments.

# Get zero-argument __init__ method for free.
empty = EmptyClass()

# Calls the __init__ method for SingleArgClass
# with arg1 set to "an arg".
single = SingleArgClass("an arg")

# Each of these calls the __init__ method for
# TwoArgClass with arg1 set to the first argument
# and arg2 set to the second argument. 
two1 = TwoArgClass(1, 2)
two2 = TwoArgClass(3, 4)


# Can also instantiate a class with the different types
# of unpacking we talked about earlier.

arg_list = [30, 40]
two3 = TwoArgClass(*arg_list)

arg_dict = {"arg2": 10, "arg1": 20}
two4 = TwoArgClass(**arg_dict)




class Box:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def increment_dimensions(self):
        self.length += 1
        self.width += 1
        self.height += 1

    # Used when str() is called on an instance.
    # Creates an "informal" string for an object.
    # If not defined for a class, the default
    # implementation calls __repr__.
    def __str__(self):
        return f"({self.length}, {self.width}, {self.height})"
 
    # Creates the canonical/formal string for an object.
    def __repr__(self):
        return (f'{self.__class__.__name__}('
           f'{self.length!r}, {self.width!r}, {self.height!r})')
