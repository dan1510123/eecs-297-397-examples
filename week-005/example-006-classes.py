# The first argument represents the class instance
# calling a particular method.
# Using 'self' is a Python convention
class Box:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h

    def double_dimensions(self):
        self.length *= 2
        self.width *= 2
        self.height *= 2

    def __repr__(self):
        return f"Box({self.length}, {self.width}, {self.height})"

# Instantiating a Box object. Behind the scenes,
# an object is created and __init__ is called.
good_box = Box(1, 2, 3)
print("Original Box:", good_box)

good_box.double_dimensions()
print("Bigger Box:", good_box)

Box.double_dimensions(good_box)
print("Biggest Box:", good_box)

print()


# Using a different name other than 'self' will 
# work, but will make your code much harder to read.
# File this under things you should not do!
class SillyBox:
    def __init__(garbage, length, width, height):
        garbage.length = length
        garbage.width = width
        garbage.height = height
        garbage.silly_factor = 100

    def double_dimensions(anythingworks):
        anythingworks.length *= 2
        anythingworks.width *= 2
        anythingworks.height *= 2

    def be_silly(athing):
        print(f"I am being silly times {athing.silly_factor}")

    def __repr__(s):
        return f"SillyBox({s.length}, {s.width}, {s.height})"

silly_box = SillyBox(5, 4, 3)
print("Silly box:", silly_box)
silly_box.double_dimensions()
print("Bigger silly box:", silly_box)



### What happens if we try to call SillyBox.double_dimensions(good_box)?
### What about SillyBox.be_silly(good_box)?

