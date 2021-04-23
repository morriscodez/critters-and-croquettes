
from exercises.petting_zoo import PettingZoo, PuddlePond, SlitherInn
from animals import mr_madof, mr_careful, mr_charm, mr_curly, miss_chill, miss_fuzz, miss_goldy, miss_misty, miss_wise, mr_flower, mr_gentle, mr_strong, mr_tiny, ms_buzz, dr_quack
from attractions import Cuddle_Cove

# miss_fuzz.chip_number = 2323232
# print("ID #:", miss_fuzz.chip_number)

NashvillePets = PettingZoo("Nashville Petting Zoo")

NashvillePets.animals.append(miss_chill)
NashvillePets.animals.append(miss_fuzz)


# print("animals desc:", NashvillePets.description)
# print("animals list:", list(NashvillePets.animals))
print(NashvillePets.last_critter_added)