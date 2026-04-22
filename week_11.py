from random import choice
from datetime import datetime
class Cat():
    def __init__(self, cat_name, coat_colour, birth_year):
        self.name = cat_name
        self.coat = coat_colour
        self.does_meow = choice([True, False])
        self.__birth_year = datetime(birth_year, 1 , 1)


    def age(self):
        age_calc = (datetime.now() - self.__birth_year).days / 365.25
        return age_calc


    def meow(self):
        if self.does_meow:
            print(f"{self.name} says meow")
        else:
            print(f"{self.name} looks at your reproachfully")

loofy = Cat("Loofy","ginger", 1977)
rufus = Cat("Rufus", "black", 2026)
print(loofy.age())
print(rufus.age())
print(loofy.name)
print(rufus.name)
print(loofy.does_meow)

(loofy.meow())
print(rufus.meow())

print(dir(loofy))
#print(type(loofy.meow))
#print(type(loofy.name))
print(loofy.name)
loofy.name = "Maya"
print(loofy.name)