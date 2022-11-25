class Liquid:

    def __init__(self, name, density):
        self.name = name
        self.density = density

    def get_volume(self, mass):
        return self.density * mass

    def set_density(self, new_density):
        self.density = new_density

    def get_mass(self, volume):
        return volume / self.density

    def print_info(self):
        print(self.name)
        print(self.density)


class Alcohol(Liquid):

    def __init__(self, strength, name, density):
        super().__init__(name, density)
        self.strength = strength

    def set_strength(self, new_strength):
        self.strength = new_strength

    def print_info(self):
        super().print_info()
        print(self.strength)

    def get_volume(self, mass):
        return [self.density * mass, (self.density * mass)*self.strength/100]


test_1 = Alcohol(40, "vodka", 980)
test_1.print_info()
print(test_1.get_volume(1))
