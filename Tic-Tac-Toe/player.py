import math
import random

class Player:
    def __init__(self,letter):
        #letter is x or 0
        self.letter = letter

    def get_move(self,game):
        pass

class RandomComputer(Player):
    def __init__(self,letter):
        super.__init__(letter)

    def get_move(self,game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super.__init__(letter)

    def get_move(self, game):
        pass
