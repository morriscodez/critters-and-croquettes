from datetime import date

class Llama:


    def __init__(self, name, species, shift, food, chip_num):


        self.name = name
        self.species = species
        self.shift = shift
        self.walling = True
        self.slithering = False
        self.swimming = False
        self.date_added = date.today()
        self.food = food
        self.__chip_number = chip_num

    def feed(self):
        print(f"{self.name} was fed {self.food} on {date.today().strftime('%m/%d/%Y')}")


    def __str__(self):
        return f"{self.name} is a majestic {self.species}"

    
    #Getter
    @property
    def chip_number(self):
        return self.__chip_number
    
    #Setter
    @chip_number.setter
    def chip_number(self, number):
        pass




