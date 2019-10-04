class SomeClass:
    
    # Class variables.
    # Shared across classes, but follows normal
    # mutable/immutable rules. Use class variables sparingly since they
    # can cause hard to debug errors (similar to global variables).
    # Always try to restructure code to remove class variables if possible, and
    # if you must use them then exercise extreme caution.

    # Modifying an int with one instance will not
    # change the same int for other instances (or the class)
    class_var_int = 10

    # Modifying this list (appending, removing, etc.) will change
    # the state of the list for all instances of the class as
    # well as for the class itself.
    class_var_list = []


    def __init__(self, a, b, c):
        # Instance variable.
        # Unique to each instance.
        self.a = a
        self.b = b
        self.c = c

    def append_args(self):
        self.c.append(self.a)
        self.c.append(self.b)

    def __repr__(self):
        return f"SomeClass(a={self.a}, b={self.b}, c={self.c})"



# These lines will make instances by passing three arguments to init
sc1 = SomeClass(1, 2, [])
sc2 = SomeClass(9, 8, [])


# All class ints start out the same
print("Initial Vals:", sc1.class_var_int, sc2.class_var_int, SomeClass.class_var_int)


# Modifying a class variable int on one instance changes nothing for the others
sc1.class_var_int += 57
print("One int modified:", sc1.class_var_int, sc2.class_var_int, SomeClass.class_var_int)

print()

# Modifying an instance variable only changes state for that instance
print("Before:", sc1, sc2)

sc1.append_args()
sc2.a, sc2.b = -5, -10

print("Change sc1 list, sc2 ints:", sc1, sc2)

print()

# Modifying a class variable list (or other mutable object) changes the state everywhere
print("Initial List:", sc1.class_var_list, sc2.class_var_list, SomeClass.class_var_list)

sc1.class_var_list.append("str1")
sc2.class_var_list.append("str2")
SomeClass.class_var_list.append("str3")

print("All modified:", sc1.class_var_list, sc2.class_var_list, SomeClass.class_var_list)



