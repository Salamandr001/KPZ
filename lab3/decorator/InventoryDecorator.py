class InventoryDecorator:
    def __init__(self, hero):
        self.hero = hero

    def attack(self):
        return self.hero.attack()

class SwordDecorator(InventoryDecorator):
    def attack(self):
        return f"{self.hero.attack()} with a sword"

class ShieldDecorator(InventoryDecorator):
    def attack(self):
        return f"{self.hero.attack()} with a shield"

class ArmorDecorator(InventoryDecorator):
    def attack(self):
        return f"{self.hero.attack()} wearing armor"
