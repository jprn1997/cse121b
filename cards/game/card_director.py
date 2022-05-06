from game.card import Card

class CardDirector():

    def __init__(self):

        #What other things need to be updated?
        self.is_playing = True
        self.score = 300
        self.total_score = 300
        self.card = Card()                              #Created the object card from class Card

    def start_game(self):
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        print(f'The card is: {self.card.old_value}')
        self.card.get_guess()

        # Change this to "Play again: [y/n]"
        # draw_card = input("Draw card? [y/n] ")
        # self.is_playing = (draw_card == "y")

    def do_updates(self):
        if not self.is_playing:
            return
        self.card.pull_card()
        #We need to do the part for doing the updates.

    def do_outputs(self):
        if not self.is_playing:
            return

        #We need to figure out how to get values and what values.
        print(f"Next card was: {self.card.new_value}")
        print(f'Your score is: {self.card.points}')
        print(f'Your total score is: {self.total_score}')
        print()
        self.is_playing = (self.total_score > 0) 