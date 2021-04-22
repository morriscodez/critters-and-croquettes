from datetime import date


class Eel:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = False
        self.swimming = True
        self.slithering = True