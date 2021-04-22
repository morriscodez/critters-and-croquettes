from datetime import date

class Tortoise:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.swimming = False
        self.slithering = False