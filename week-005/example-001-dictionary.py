def print_animal_sound(sounds, animal, default_sound="?"):
    print(f"The {animal} goes", sounds.get(animal, default_sound))



# Making a dictionary. Can be empty or can be made
# with a set of comma separated key: value pairs.


empty_dict = {}
animal_sounds = {"cat": "meow", "dog": "woof", "cow": "moo"}


# Can add items
animal_sounds["horse"] = "neigh"


other_key = "crow"
other_value = "caw"

animal_sounds[other_key] = other_value


### How can we modify an item in a dictionary?


# Can get value associated with a key
print(animal_sounds["horse"])

# Can also use get(). Doing so allows you to specify
# a default value if the key is not found in the dictionary
print_animal_sound(animal_sounds, "cat")

# Will return "?" if the key does not exist
print_animal_sound(animal_sounds, "owl")


# Now we return the right sound since we added the key
# value pair to the dictionary
animal_sounds["owl"] = "who"
print_animal_sound(animal_sounds, "owl")


### How can we delete an item in a dictionary?
