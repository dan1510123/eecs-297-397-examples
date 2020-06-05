class Series(object):
    def __init__(self, low_value, high_value):
        self.low_value = low_value
        self.high_value = high_value

    def __iter__(self):
        self.current_value = self.low_value
        return self

    def __next__(self):
        if self.current_value < self.high_value:
            self.current_value += 1
            return self.current_value - 1
        else:
            # Part of the iterator protocol is to raise StopIteration
            # when there are no more values to iterate over.
            raise StopIteration

series = Series(1, 5)

# Since Series implements __iter__ and __next__, we
# can use Series anywhere an Iterable is expected.
# Examples:
for num in series:
    print("In for loop", num)

print("Created a list:", list(series))


# Can also call iter() and next() by hand.
# Note: Due to the __iter__() method implementation,
#       series_iterator is the same object as series.
#       Sometimes iterators will return an entirely new object (like in example_002_separate_iterator.py).
series_iterator = iter(series)
try:
    while True:
        print("Calling next in while loop:", next(series_iterator))
except StopIteration:
    pass
