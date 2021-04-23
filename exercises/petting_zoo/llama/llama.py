from datetime import date
from exercises.petting_zoo.animal import Animal
from exercises.petting_zoo import 

class Llama(Animal):


    def __init__(self, name, species, shift, food, chip_num):


        super().__init__(self, name, species, shift, food, chip_num)
        self.shift = shift
        self.walking = True

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




