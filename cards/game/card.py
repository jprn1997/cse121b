import random

"""class Card is used to create the Card object with values and gets
user guess of Hi or Lo and finally declares points based on what was retrieved."""
class Card():

    """Creates card object and declares attributes."""
    def __init__(self):
        self.value = 0
        self.points = 0
        self.guess = 0

    """method to to collect input for which """
    def guess(self):
        self.guess = input("Hi or Low: ")

    """method to pull a card with a random number between 1 and 13.
    It then will assign points based on the guess that was made with the guess method."""
    def pull_card(self):
        self.value = random.randint(1, 13)
        self.points = 100 if self.guess == "Hi" and self.guess > self.value else 100 if self.guess == "Low" and self.guess < self.value else -75