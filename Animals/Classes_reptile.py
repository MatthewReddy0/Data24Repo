from Classes_animal import *


class Reptile(Animal):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self.tetrapod = None
        self.heart_chamber = [3, 4]

gekko = Reptile()
print(gekko.alive)
