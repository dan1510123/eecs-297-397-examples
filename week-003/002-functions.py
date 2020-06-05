#!/usr/local/bin/python3

# Can declare a function using def.

# This function takes no arguments.
def print_some_message():
    print("Hello from a function")


# Can't use functions until they are defined!
# Next line will throw an error if uncommented.
#print_repeat_message("broken", 10)


# This function takes two arguments.
def print_repeat_message(message, number_of_times):
    for i in range(number_of_times):
        print(message)


# Running this code will do nothing.
# We have to call the function in 
# order for the code to execute.
