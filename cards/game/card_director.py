from game.card import Card

class CardDirector():

    def __init__(self):

        #What other things need to be updated?
        self.is_playing = True
        self.score = 300
        self.total_score = ""

    def start_game(self):
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        draw_card = input("Draw card? [y/n] ")
        self.is_playing = (draw_card == "y")

    def do_updates(self):
        if not self.is_playing:
            return
        #We need to do the part for doing the updates.

    def do_outputs(self):
        if not self.is_playing:
            return

        values = ""
        #We need to figure out how to get values and what values.

        print(f'You drew: {values}')
        print(f'Your score is: {self.score}\n')
        print(f'Your total score is: {self.total_score}')
        self.is_playing == (self.total_score > 0)