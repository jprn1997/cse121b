import random

class Card():

    def __init__(self):
        self.value = 0
        self.points = 0
        self.guess = 

    def guess(self)

    def pull_card(self):
        self.value = random.randint(1, 13)
        self.points = 50 if self.value == 6 else 100 if self.value == 1 else 0