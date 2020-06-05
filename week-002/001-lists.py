#!/usr/local/bin/python3

# Make an empty list

colors = []



# Make a populated list

fruits = ["apple", "banana", "orange", "watermelon"]



# Lists have random access. Index starts at 0.

print(fruits[0])        # apple

print(fruits[2])        # orange

# Next line would throw an error
# print(colors[0])


# Can use negative index syntax to access elements from end of list

print(fruits[-1])       # last element in list (watermelon)

print(fruits[-3])       # third item from end (banana)
