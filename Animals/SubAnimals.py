from MainAnimals import *


class Dolphin:
    def __init__(self):
        super(Mammal).__init__()
        self.size = 'Larger than a dog'
        self.carnivore = 'Carnivore'
        self.legs = '0 legs'
        self.fly = 'Cannot fly'


class Human:
    def __init__(self):
        super(Mammal).__init__()
        self.size = 'Larger than a dog'
        self.carnivore = 'Not a carnivore'
        self.legs = '4 legs'
        self.fly = 'Cannot fly'


class Platypus:
    def __init__(self):
        super(Mammal).__init__()
        self.size = 'Between a rat and a dog'
        self.carnivore = 'Carnivore'
        self.legs = '4 legs'
        self.fly = 'Cannot fly'


class Bat:
    def __init__(self):
        super(Mammal).__init__()
        self.size = 'Smaller than a rat'
        self.carnivore = 'Carnivore'
        self.legs = '2 legs'
        self.fly = 'Flies'


class PolarBear:
    def __init__(self):
        super(Mammal).__init__()
        self.size = 'Larger than a dog'
        self.carnivore = 'Carnivore'
        self.legs = '4 legs'
        self.fly = 'Cannot fly'


class FieldMouse:
    def __init__(self):
        super(Mammal).__init__()
        self.size = 'Smaller than a rat'
        self.carnivore = 'Not a carnivore'
        self.legs = '4 legs'
        self.fly = 'Cannot fly'


class Deer:
    def __init__(self):
        super(Mammal).__init__()
        self.size = 'Larger than a dog'
        self.carnivore = 'Not a carnivore'
        self.legs = '4 legs'
        self.fly = 'Cannot fly'


"""
Mammal – Dolphin, Human, Platypus, Bat, Polar bear, Field mouse, Deer

Bird – Kiwi, Ostrich, Eagle, Hummingbird, Swans, Toucans

Reptile – Corn Snake, Gila monster, Crocodile, Gecko, Anaconda, Dryland tortoise (non-carnivorous)

Amphibians – Red-eyed tree frog, Goliath frog, Giant Salamander
"""


class Kiwi:
    def __init__(self):
        super(Bird).__init__()
        self.size = 'Smaller than a rat'
        self.carnivore = 'Not a carnivore'
        self.legs = '2 legs'
        self.fly = 'Cannot fly'


class Ostrich:
    def __init__(self):
        super(Bird).__init__()
        self.size = 'Larger than a dog'
        self.carnivore = 'Not a carnivore'
        self.legs = '2 legs'
        self.fly = 'Cannot fly'


class Eagle:
    def __init__(self):
        super(Bird).__init__()
        self.size = 'Between a rat and a dog'
        self.carnivore = 'Carnivore'
        self.legs = '2 legs'
        self.fly = 'Flies'


class Hummingbird:
    def __init__(self):
        super(Bird).__init__()
        self.size = 'Smaller than a rat'
        self.carnivore = 'Not a carnivore'
        self.legs = '2 legs'
        self.fly = 'Flies'


class Swan:
    def __init__(self):
        super(Bird).__init__()
        self.size = 'Larger than a dog'
        self.carnivore = 'Not a carnivore'
        self.legs = '2 legs'
        self.fly = 'Flies'


class Toucan:
    def __init__(self):
        super(Bird).__init__()
        self.size = 'Between a rat and a dog'
        self.carnivore = 'Not a carnivore'
        self.legs = '2 legs'
        self.fly = 'Flies'


"""
Mammal – Dolphin, Human, Platypus, Bat, Polar bear, Field mouse, Deer

Bird – Kiwi, Ostrich, Eagle, Hummingbird, Swans, Toucans

Reptile – Corn Snake, Gila monster, Crocodile, Gecko, Anaconda, Dryland tortoise (non-carnivorous)

Amphibians – Red-eyed tree frog, Goliath frog, Giant Salamander
"""


class CornSnake:
    def __init__(self):
        super(Reptile).__init__()
        self.size = 'Between a rat and a dog'
        self.carnivore = 'Carnivore'
        self.legs = '0 legs'
        self.fly = 'Cannot fly'


class GilaMonster:
    def __init__(self):
        super(Reptile).__init__()
        self.size = 'Between a rat and a dog'
        self.carnivore = 'Carnivore'
        self.legs = '4 legs'
        self.fly = 'Cannot fly'


class Crocodile:
    def __init__(self):
        super(Reptile).__init__()
        self.size = 'Larger than a dog'
        self.carnivore = 'Carnivore'
        self.legs = '4 legs'
        self.fly = 'Cannot fly'


class Gecko:
    def __init__(self):
        super(Reptile).__init__()
        self.size = 'Smaller than a rat'
        self.carnivore = 'Carnivore'
        self.legs = '4 legs'
        self.fly = 'Cannot fly'


class Anaconda:
    def __init__(self):
        super(Reptile).__init__()
        self.size = 'Larger than a dog'
        self.carnivore = 'Carnivore'
        self.legs = '0 legs'
        self.fly = 'Cannot fly'


class DrylandTortoise:
    def __init__(self):
        super(Reptile).__init__()
        self.size = 'Between a rat and a dog'
        self.carnivore = 'Not a carnivore'
        self.legs = '4 legs'
        self.fly = 'Cannot fly'


"""
Mammal – Dolphin, Human, Platypus, Bat, Polar bear, Field mouse, Deer

Bird – Kiwi, Ostrich, Eagle, Hummingbird, Swans, Toucans

Reptile – Corn Snake, Gila monster, Crocodile, Gecko, Anaconda, Dryland tortoise (non-carnivorous)

Amphibians – Red-eyed tree frog, Goliath frog, Giant Salamander
"""


class RedEyedTreeFrog:
    def __init__(self):
        super(Amphibian).__init__()
        self.size = 'Smaller than a rat'
        self.carnivore = 'Carnivore'
        self.legs = '4 legs'
        self.fly = 'Cannot fly'


class GoliathFrog:
    def __init__(self):
        super(Amphibian).__init__()
        self.size = 'Between a rat and a dog'
        self.carnivore = 'Not a carnivore'
        self.legs = '4 legs'
        self.fly = 'Cannot fly'


class GiantSalamander:
    def __init__(self):
        super(Amphibian).__init__()
        self.size = 'Larger than a dog'
        self.carnivore = 'Carnivore'
        self.legs = '4 legs'
        self.fly = 'Cannot fly'
