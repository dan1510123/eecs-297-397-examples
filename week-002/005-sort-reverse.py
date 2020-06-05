#!/usr/local/bin/python3

numbers = [9, 3, 2, 4, 10, 34, 56, 73, 3, 2, 1]

print(numbers)


# Can get a new copy of the list sorted with sorted().
# Original list remains the same

sorted_numbers = sorted(numbers)

print(sorted_numbers)
print(numbers)


# Can sort a list in place with sort()

numbers.sort()
print(numbers)         # now numbers is sorted too


# Can also reverse a list in place with reverse()
foods = ["butter", "popcorn", "cheese"]

print(foods)
foods.reverse()
print(foods)

# Can reverse sort too

reverse_sorted_foods = sorted(foods, reverse = True)
print(reverse_sorted_foods)

foods.sort(reverse = True)          # reverse sort foods in place
print(foods)
