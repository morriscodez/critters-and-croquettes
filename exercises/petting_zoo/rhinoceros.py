from datetime import date


class Rhinoceros:

    def __init__(self):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True
        self.swimming = True
        self.slithering = False