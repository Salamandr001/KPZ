from Warrior import Warrior
from Mage import Mage
from Palladin import Palladin
from InventoryDecorator import SwordDecorator, ShieldDecorator, ArmorDecorator

def main():
    warrior = Warrior()
    mage = Mage()
    palladin = Palladin()

    print(warrior.attack())
    print(mage.attack())
    print(palladin.attack())

    # Decorating with inventory
    sword_warrior = SwordDecorator(warrior)
    shield_mage = ShieldDecorator(mage)
    armor_palladin = ArmorDecorator(palladin)

    print(sword_warrior.attack())
    print(shield_mage.attack())
    print(armor_palladin.attack())

    # Multiple decorators
    armored_sword_warrior = ArmorDecorator(SwordDecorator(warrior))
    print(armored_sword_warrior.attack())

if __name__ == '__main__':
    main()
