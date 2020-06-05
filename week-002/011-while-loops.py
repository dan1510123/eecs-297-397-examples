#!/usr/local/bin/python3

numbers = list(range(10))

print(numbers)

while len(numbers) > 5:
    del numbers[-1]

print(numbers)
