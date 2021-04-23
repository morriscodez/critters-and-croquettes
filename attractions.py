
from exercises.petting_zoo import PettingZoo, PuddlePond, SlitherInn
from animals import mr_madof, mr_careful, mr_charm, mr_curly, miss_chill, miss_fuzz, miss_goldy, miss_misty, miss_wise, mr_flower, mr_gentle, mr_strong, mr_tiny, ms_buzz, dr_quack


Reptile_Row = SlitherInn("Reptile Row")
Peach_Pond = PuddlePond("Peach Pond")
Cuddle_Cove = PettingZoo("Cuddle Cove")


Reptile_Row.animals.append(mr_madof)
Reptile_Row.animals.append(mr_charm)
Reptile_Row.animals.append(mr_tiny)
Reptile_Row.animals.append(miss_goldy)
Reptile_Row.animals.append(mr_flower)
Peach_Pond.animals.append(ms_buzz)
Peach_Pond.animals.append(dr_quack)
Peach_Pond.animals.append(miss_misty)
Peach_Pond.animals.append(mr_gentle)
Peach_Pond.animals.append(miss_wise)
Cuddle_Cove.animals.append(mr_strong)
Cuddle_Cove.animals.append(mr_curly)
Cuddle_Cove.animals.append(miss_fuzz)
Cuddle_Cove.animals.append(miss_chill)
Cuddle_Cove.animals.append(mr_careful)

for animal in Reptile_Row.animals:
    print(f'You can find {animal.name} the {animal.species} in {Reptile_Row.attraction_name}')

for animal in Peach_Pond.animals:
    print(f'You can find {animal.name} the {animal.species} in {Peach_Pond.attraction_name}')

for animal in Cuddle_Cove.animals:
    print(f'You can find {animal.name} the {animal.species} in {Cuddle_Cove.attraction_name}')