empty_set = set()

animal_set = set(["cat", "cat", "dog", "elephant"])

print(animal_set)

# Can check for items in a set
if "cat" in animal_set:
    print("cat was in the set")


# Run this multiple times. You may see the ordering
# change between runs
for animal in animal_set:
    print(animal)


frozen_set = frozenset([x ** 2 for x in range(20)])

print(frozen_set)

### Look through help(frozenset). How do the functions there
### compare to help(set)?
