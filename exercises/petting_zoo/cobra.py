from datetime import date


class Cobra:

    def __init__(self):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = False
        self.swimming = False
        self.slithering = True