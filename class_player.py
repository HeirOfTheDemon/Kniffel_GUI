# Diese Spielerklasse wurde erzeugt für die Idee
# der Verfolgung, Berechnung und Ausgabe der Punkte.
# Die Implementierung folgt in Version 2.0

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
