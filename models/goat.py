from datetime import date


class Goat:

    def __init__(self):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True
        self.swimming = False
        self.slithering = False