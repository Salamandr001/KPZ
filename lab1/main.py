from animal import Mammal, Bird
from enclosure import Enclosure
from food import Food
from employee import Employee
from inventory import Inventory

def main():
    # Creating animals
    lion = Mammal(name="Leo", species="Lion", age=5, fur_color="golden")
    parrot = Bird(name="Polly", species="Parrot", age=2, wing_span=0.5)

    # Creating enclosures
    savannah = Enclosure(enclosure_type="Savannah", size=1000)
    aviary = Enclosure(enclosure_type="Aviary", size=300)

    # Adding animals to enclosures
    savannah.add_animal(lion)
    aviary.add_animal(parrot)

    # Creating food
    meat = Food(food_type="Meat", quantity=50)
    seeds = Food(food_type="Seeds", quantity=10)

    # Creating employees
    keeper = Employee(name="John Doe", role="Zookeeper")
    vet = Employee(name="Jane Smith", role="Veterinarian")

    # Creating inventory
    zoo_inventory = Inventory()

    # Adding items to inventory
    zoo_inventory.add_animal(lion)
    zoo_inventory.add_animal(parrot)
    zoo_inventory.add_enclosure(savannah)
    zoo_inventory.add_enclosure(aviary)
    zoo_inventory.add_food(meat)
    zoo_inventory.add_food(seeds)
    zoo_inventory.add_employee(keeper)
    zoo_inventory.add_employee(vet)

    # Displaying inventory
    print(zoo_inventory)

if __name__ == "__main__":
    main()
