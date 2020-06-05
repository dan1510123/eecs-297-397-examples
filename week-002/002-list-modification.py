#!/usr/local/bin/python3

numbers = [3, 5, 7, 11, 13, 17, 19]
print(numbers)

# Can modify list entries in place

numbers[1] = "used to be 5"
numbers[-2] = "used to be 17"

print(numbers)



# Can add elements to end of list with append()

numbers.append(55)
numbers.append(103)
print(numbers)



# Can insert into arbitary positions with insert()

numbers.insert(1, 1000)        # second item in list is now 1000
                               # other items shifted to the right
print(numbers)
