from datetime import date

class Tortoise:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.swimming = False
        self.slithering = False

    def feed(self):
        print(f"{self.name} was fed {self.food} on {date.today().strftime('%m/%d/%Y')}")


    def __str__(self):
        return f"{self.name} is a majestic {self.species}"