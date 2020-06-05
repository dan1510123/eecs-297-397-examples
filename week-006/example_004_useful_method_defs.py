class MethodExampleClass:
    def __init__(self, val):
        self.val = val

    # Supports syntax  if class_instance:
    #
    # 'not' supported for free 
    def __bool__(self):
        return self.val > 0

    # Supports sorting instances of this class
    def __lt__(self, other):
        return self.val < other.val

    # Custom equality logic.
    def __eq__(self, other):
        return self.val == other.val

    # Needed to support set insertion/using class
    # as a key in a dict
    def __hash__(self):
        return hash(self.val)

    def __repr__(self):
        return f"MethodExampleClass({self.val})"

mec_1 = MethodExampleClass(10)
mec_2 = MethodExampleClass(0)

if mec_1:
    print(mec_1, "was true")

if not mec_2:
    print(mec_2, "was false")

mec_list = [mec_1, mec_2]
print(mec_list)

print(sorted(mec_list))



class IteratorExample:
    def __init__(self, *args):
        self.values = args

    # Pattern when whatever we want to iterate over
    # already has iterator functionality
    def __iter__(self):
        return iter(self.values)

for v in IteratorExample(1, 2, 3, 4, 5, 6, 7):
    print(v, end=' ')
print()



class BoxIteratorExample:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h

    # Can cheat, and put whatever we want to iterate over
    # in a list and return iter(the list).
    #
    # If interested, read up on Python generators and 
    # iterators to cover more complicated/general examples.
    def __iter__(self):
        return iter([self.length, self.width, self.height])


bi_example = BoxIteratorExample(10, 5, 3)
for measurement in bi_example:
    print(measurement, end=' ')
print()
