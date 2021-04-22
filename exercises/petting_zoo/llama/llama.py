from datetime import date

class Llama:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.walling = True
        self.slithering = False
        self.swimming = False
        self.date_added = date.today()


