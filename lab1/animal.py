class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def __str__(self):
        return f"{self.name} is a {self.species} aged {self.age} years."


class Mammal(Animal):
    def __init__(self, name, species, age, fur_color):
        super().__init__(name, species, age)
        self.fur_color = fur_color

    def __str__(self):
        return f"{self.name} is a {self.species} with {self.fur_color} fur, aged {self.age} years."


class Bird(Animal):
    def __init__(self, name, species, age, wing_span):
        super().__init__(name, species, age)
        self.wing_span = wing_span

    def __str__(self):
        return f"{self.name} is a {self.species} with a wingspan of {self.wing_span} meters, aged {self.age} years."
