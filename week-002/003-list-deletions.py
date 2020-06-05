#!/usr/local/bin/python3

numbers = [3, 5, 7, 11, 13, 17, 19]
print(numbers)


# Can delete an item with del

del numbers[2]         # 7 removed from list
print(numbers)



# Can remove and retrieve an item with pop()

second_item = numbers.pop(1)                # get second item
print(second_item)
print(numbers)

last_item = numbers.pop()                   # get last item
print(last_item)
print(numbers)


# Can remove item by value with remove()
numbers.remove(17)
print(numbers)


