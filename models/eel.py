from datetime import date


class Eel:

    def __init__(self):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = False
        self.swimming = True
        self.slithering = True