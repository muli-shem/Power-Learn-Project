# Base class
class Superhero:
    def __init__(self, name, power, universe):
        self.name = name
        self.power = power
        self.universe = universe

    def introduce(self):
        print(f"I am {self.name} from {self.universe} and my power is {self.power}!")

    def use_power(self):
        print(f"{self.name} uses their superpower: {self.power}!")

# Inherited class (demonstrating polymorphism + encapsulation)
class FlyingHero(Superhero):
    def use_power(self):
        print(f"{self.name} takes off into the sky! Flying high with super speed!")

class StrengthHero(Superhero):
    def use_power(self):
        print(f"{self.name} smashes through walls with super strength!")

# Create objects
hero1 = FlyingHero("SkyBlade", "Flight", "Marvel")
hero2 = StrengthHero("IronFist", "Super Strength", "DC")

# Use methods
hero1.introduce()
hero1.use_power()

hero2.introduce()
hero2.use_power()
