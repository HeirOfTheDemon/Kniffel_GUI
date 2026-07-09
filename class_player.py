import game_window as gw

class Player:
    number_players = []

    def __init__(self, name):
        self.name = name
# Setter und getter der Player-Klasse
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score

    #gw.button_cell(1,1)
