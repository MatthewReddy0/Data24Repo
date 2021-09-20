from SubAnimals import *

animal = think_of_animal()

list_of_animals = ['hyena', 'field mouse', 'dolphin', 'human', 'cheetah', 'elephant', 'bat', 'squirrel', 'whale',
                   'hedgehog', 'rabbit', 'fox', 'deer', 'seal', 'polar bear', 'platypus',
                   'kiwi', 'ostrich', 'eagle', 'hummingbird', 'swans', 'toucans',
                   'corn Snake', 'komodo dragon', 'crocodile', 'gecko', 'chameleon', 'anaconda', 'dryland tortoise',
                   'red-eyed tree frog', 'bullfrog', 'giant salamander']

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
    if playerinput.lower() == animal:
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
