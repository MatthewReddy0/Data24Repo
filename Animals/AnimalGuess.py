from SubAnimals import *
import random

animal_list = (Dolphin, Human, Platypus, Bat, PolarBear, FieldMouse, Deer,
           Kiwi, Ostrich, Eagle, Hummingbird, Swan, Toucan,
           CornSnake, GilaMonster, Crocodile, Gecko, Anaconda, DrylandTortoise,
           RedEyedTreeFrog, GoliathFrog, GiantSalamander)
the_chosen_one = random.choice(animal_list)
animal = the_chosen_one()
new_animal = str(the_chosen_one)
new_animal = new_animal[:-2]
new_animal = new_animal.split('.')[1]
# print(animal)

list_of_animals = ('Dolphin', 'Human', 'Platypus', 'Bat', 'PolarBear', 'FieldMouse', 'Deer',
                   'Kiwi', 'Ostrich', 'Eagle', 'Hummingbird', 'Swan', 'Toucan',
                   'CornSnake', 'GilaMonster', 'Crocodile', 'Gecko', 'Anaconda', 'DrylandTortoise',
                   'RedEyedTreeFrog', 'GoliathFrog', 'GiantSalamander')

game_state = True
lives = 3
you = 'haven\'t finished the game.'
print('I\'m thinking of an animal')

while game_state:
    print(list_of_animals)
    print('Choose a question using the numbers, or type in the name of the animal you think I\'m thinking of')
    print(f'You haves {lives} lives')
    print('1. Is it warm-blooded? \n'
          '2. Does it lay hard-shelled eggs? \n'
          '3. What is its size? \n'
          '4. Is it a carnivore? \n'
          '5. How many legs does it have? \n'
          '6. Can it fly? \n')
    playerinput = input()
    if playerinput.lower() == new_animal:
        you = 'won!'
        game_state = False
    elif playerinput == '1':
        print(animal.warmblooded)
    elif playerinput == '2':
        print(animal.eggs)
    elif playerinput == '3':
        print(animal.size)
    elif playerinput == '4':
        print(animal.carnivore)
    elif playerinput == '5':
        print(animal.legs)
    elif playerinput == '6':
        print(animal.fly)
    elif playerinput.lower() in list_of_animals:
        print('Wrong animal!')
        lives += -1
        if lives == 0:
            you = 'lost'
            game_state = False
    else:
        print('Please enter a valid input\n\n')

print(f'You {you}')
