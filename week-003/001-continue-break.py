#!/usr/local/bin/python3

numbers = list(range(100))

print("Original List: ", end = ' ')
print(numbers, end = '\n\n')

print("Use continue to skip odd numbers")
for number in numbers:
    if number % 2 == 1:
        continue
    print(number, end = ' ')
print(end = '\n\n')




print("Use break to exit loop when we hit the first odd number")
for number in numbers:
    if number % 2 == 1:
        break
    print(number, end = ' ')
print()



print()

i = 0
while i < 10:
    # do stuff
    print(i, end=' ')
    i += 1
print()

# Or can use a break statement
j = 0
while True:
    if j >= 10:
        break
    # do stuff
    print(j, end=' ')
    j += 1
print()
