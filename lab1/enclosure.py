class Enclosure:
    def __init__(self, enclosure_type, size):
        self.enclosure_type = enclosure_type
        self.size = size
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def __str__(self):
        return f"{self.enclosure_type} enclosure of size {self.size} square meters containing {len(self.animals)} animals."
