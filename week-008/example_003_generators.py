# A generator that yields items instead of returning a list.
# Think of a generator as a function that saves its state when
# it hits a yield statement and returns that value.
# The generator will resume running where it last yielded
# when a value is requested (using next()).
# A generator yields one value at a time. When the generator
# reaches the end of its definition (stops yielding values),
# then StopIteration is raised.

def range_generator(low_value, high_value):
    """
    Similar to the built-in range().

    Generates numbers from low_value to high_value - 1.
    """
    current_value = low_value
    while current_value < high_value:
        yield current_value
        current_value += 1


# Calling range_generator() will return a generator object
range_gen = range_generator(1, 10)
print(type(range_gen))

# Can generate values one at a time using next()
first_number_generated = next(range_gen)
second_number_generated = next(range_gen)
third_number_generated = next(range_gen)

print(first_number_generated,
      second_number_generated,
      third_number_generated)

try:
    while True:
        generated_value = next(range_gen)
        print(generated_value)
except StopIteration:
    pass


# Prints out 0 - 9
for i in range_generator(1, 10):
    print(i)
