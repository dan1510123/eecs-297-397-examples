def modifies_global(value):
    global global_int
    global_int = value

def does_not_modify_global(value):
    # Assignment creates 'global_int' in the local namespace
    global_int = value
    print("Local:", locals())

def outer_function():
    x = 4
    y = 5
    print("Init x:", x, "Init y:", y)

    def inner_function_1():
        # Will start looking for 'x' in the enclosing namespace
        nonlocal x
        x = 444
        y = 555

    inner_function_1()
    print("Modified x:", x, "Same y:", y)



global_int = 10
print("Before", global_int)

modifies_global(50)
print("After modify:", global_int)

does_not_modify_global(100)
print("After does not modify:", global_int)


outer_function()