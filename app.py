import datetime



class SuperHero:
    def __init__(self, name, strength_level):
        self.name = name
        self.strength_level = strength_level

    def __str__(self) -> str:
        return self.name


    def is_stronger_than(self, other_hero):
        return self.strength_level > other_hero.strength_level


if __name__ == "__main__":
    superhero = SuperHero(name="Batman", strength_level=50)
    print(superhero.is_stronger_than(SuperHero(name="Spiderman",strength_level=20)))


        