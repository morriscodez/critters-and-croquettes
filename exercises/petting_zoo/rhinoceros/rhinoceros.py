from datetime import date


class Rhinoceros:


    def __init__(self, name, species, shift, food):

        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.food = food
        self.walking = True
        self.swimming = True
        self.slithering = False

    def feed(self):
        print(f"{self.name} was fed {self.food} on {date.today().strftime('%m/%d/%Y')}")

    def __str__(self):
        return f"{self.name} is a majestic {self.species}"