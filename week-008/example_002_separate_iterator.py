# Note that MyRange implements __iter__ to return an iterator object
# of type MyRangeIterator. The MyRangeIterator implements __next__.
class MyRange:
    def __init__(self, low_value, high_value):
        self.low_value = low_value
        self.high_value = high_value

    def __iter__(self):
        return MyRangeIterator(self)


class MyRangeIterator:
    def __init__(self, source):
        self.current_value = source.low_value
        self.high_value = source.high_value

    def __next__(self):
        if self.current_value < self.high_value:
            self.current_value += 1
            return self.current_value - 1
        else:
            raise StopIteration


my_range = MyRange(1, 10)

for number in my_range:
    print(number)


my_range_iterator = iter(my_range)
try:
    while True:
        print(next(my_range_iterator))
except StopIteration:
    pass
