from animal import Animal, Mammal, Bird
from enclosure import Enclosure
from food import Food
from employee import Employee

class Inventory:
    def __init__(self):
        self.animals = []
        self.employees = []
        self.enclosures = []
        self.foods = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def add_enclosure(self, enclosure):
        self.enclosures.append(enclosure)

    def add_food(self, food):
        self.foods.append(food)

    def __str__(self):
        return (f"Zoo Inventory:\n"
                f"Animals: {[str(animal) for animal in self.animals]}\n"
                f"Employees: {[str(employee) for employee in self.employees]}\n"
                f"Enclosures: {[str(enclosure) for enclosure in self.enclosures]}\n"
                f"Food: {[str(food) for food in self.foods]}")
