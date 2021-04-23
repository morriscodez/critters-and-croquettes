class PettingZoo:

    def __init__(self, name):

        self.attraction_name = name
        self.description = "cute and fuzzy critters to cuddle"
        self.animals = []

    #Getter
    @property
    def last_critter_added(self):
        return self.animals[-1]

        