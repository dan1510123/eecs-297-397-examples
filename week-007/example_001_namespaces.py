import builtins

# Prints out everything in the global (module-level) namespace so far.
# Note: this information is tracked in a dictionary.
print(globals())

# A variable declared here will be added to the global namespace
example_var = "I am a global example"

# Note the new entry
#    'example_var': 'I am a global example'
print(globals(), end="\n\n")


# Defining a function will create a separate namespace.
# Assigning to variables will add those bindings to the
# local namespace.
def local_namespace_example():
    print("Local before:", locals())
    local_var = "LOCAL EXAMPLE"
    print("Local after:", locals())

    # Note lack of local_var in the globals().
    # Also note the function definition for local_namespace_example is now in globals()
    print("Global after:", globals())

    # You can access items in the global namespace from within a function
    print(example_var, end="\n\n")

    # Since we referenced a global version of example_var first, trying to create a local
    # version after will break
    # example_var = "Uncomment this line to break things."

local_namespace_example()

def create_local_variable_first():
    example_var = "This is fine"
    print(example_var)


    print("Global:", globals())
    print("Local:", locals(), end="\n\n")

create_local_variable_first()


def overwrite_print():
    def reverse_print(string):
        builtins.print(string[::-1])

    # Can overwrite print temporarily. Since local namespace is searched first,
    # we will use this version any time we call print() in this function.
    print = reverse_print

    builtins.print("Local Normally:", locals(), end="\n\n")

    # Will find the overwritten version of print instead of built-in print()
    print("Global: " + str(globals()))
    print("\n\nLocal: " + str(locals()))

overwrite_print()

print("This is back to normal now!")