class Character:
    def __init__(self):
        self.attributes = {}

    def __str__(self):
        return str(self.attributes)

class Builder:
    def set_height(self, height):
        pass

    def set_body_type(self, body_type):
        pass

    def set_hair_color(self, hair_color):
        pass

    def set_eye_color(self, eye_color):
        pass

    def set_outfit(self, outfit):
        pass

    def set_inventory(self, inventory):
        pass

class HeroBuilder(Builder):
    def __init__(self):
        self.character = Character()

    def set_height(self, height):
        self.character.attributes['height'] = height
        return self

    def set_body_type(self, body_type):
        self.character.attributes['body_type'] = body_type
        return self

    def set_hair_color(self, hair_color):
        self.character.attributes['hair_color'] = hair_color
        return self

    def set_eye_color(self, eye_color):
        self.character.attributes['eye_color'] = eye_color
        return self

    def set_outfit(self, outfit):
        self.character.attributes['outfit'] = outfit
        return self

    def set_inventory(self, inventory):
        self.character.attributes['inventory'] = inventory
        return self

    def build(self):
        return self.character

class EnemyBuilder(Builder):
    def __init__(self):
        self.character = Character()

    def set_height(self, height):
        self.character.attributes['height'] = height
        return self

    def set_body_type(self, body_type):
        self.character.attributes['body_type'] = body_type
        return self

    def set_hair_color(self, hair_color):
        self.character.attributes['hair_color'] = hair_color
        return self

    def set_eye_color(self, eye_color):
        self.character.attributes['eye_color'] = eye_color
        return self

    def set_outfit(self, outfit):
        self.character.attributes['outfit'] = outfit
        return self

    def set_inventory(self, inventory):
        self.character.attributes['inventory'] = inventory
        return self

    def build(self):
        return self.character

class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        return (self.builder
                .set_height("6 feet")
                .set_body_type("Athletic")
                .set_hair_color("Brown")
                .set_eye_color("Blue")
                .set_outfit("Armor")
                .set_inventory(["Sword", "Shield"])
                .build())

# Client Code
def main():
    hero_builder = HeroBuilder()
    enemy_builder = EnemyBuilder()
    director = Director(hero_builder)
    hero = director.construct()
    print("Hero:", hero)

    director = Director(enemy_builder)
    enemy = director.construct()
    print("Enemy:", enemy)

if __name__ == "__main__":
    main()
