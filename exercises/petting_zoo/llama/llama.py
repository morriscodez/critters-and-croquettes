from datetime import date

class Llama:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.walling = True
        self.slithering = False
        self.swimming = False
        self.date_added = date.today()


