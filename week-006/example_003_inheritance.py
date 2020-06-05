class Material:
    def __init__(self):
        self.material = "straw"

    def upgrade(self):
        if self.material == "straw":
            self.material = "twig"
        elif self.material == "twig":
            self.material = "stone"

    def __repr__(self):
        return self.material

class Size:
    def __init__(self):
        self.size = "small"
    
    def upgrade(self):
        if self.size == "small":
            self.size = "medium"
        elif self.size == "medium":
            self.size = "large"
    
    def __repr__(self):
        return self.size

class DescriptiveSize(Size):
    def __init__(self, adjective):
        super(DescriptiveSize, self).__init__()
        self.adjective = adjective

    def __repr__(self):
        return f"{self.adjective} {super(DescriptiveSize, self).__repr__()}"




class PigHouse(Size, Material):
    def __init__(self):
        Material.__init__(self)
        Size.__init__(self)

    def __repr__(self):
        return f"{Size.__repr__(self)} {Material.__repr__(self)} house"

pig_house = PigHouse()
print(pig_house)


### What happens if we call pig_house.upgrade() ?

#pig_house.upgrade()
#print(pig_house)




# Methods and variables will be searched for in the order
# specified by __mro__ for a Class
#print(PigHouse.__mro__)

# mro -> method resolution order

# When an appropriate method or variable is found the
# search stops. In the example above, upgrade()
# is only called from Size, and not from Material.
