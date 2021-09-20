from Classes_reptile import *


class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.venom = None
        self.surprise_attack()


    def surprise_attack(self):
        print('Gotcha!!!')


sally = Snake()
