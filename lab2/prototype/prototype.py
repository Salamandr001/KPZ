import copy

class Virus:
    def __init__(self, weight, age, name, species):
        self.weight = weight
        self.age = age
        self.name = name
        self.species = species
        self.children = []

    def clone(self):
        clone_obj = copy.deepcopy(self)
        return clone_obj

    def add_child(self, child):
        self.children.append(child)

# Client Code
def main():
    parent_virus = Virus(1.5, 2, "ParentVirus", "TypeA")
    child_virus1 = Virus(1.0, 1, "ChildVirus1", "TypeA")
    child_virus2 = Virus(0.8, 1, "ChildVirus2", "TypeA")

    parent_virus.add_child(child_virus1)
    parent_virus.add_child(child_virus2)

    cloned_virus = parent_virus.clone()

    print(f"Original: {parent_virus.name}, Children: {[child.name for child in parent_virus.children]}")
    print(f"Clone: {cloned_virus.name}, Children: {[child.name for child in cloned_virus.children]}")

if __name__ == "__main__":
    main()
