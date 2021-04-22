from datetime import date



class Mallard:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True
        self.swimming = True
        self.slithering = False