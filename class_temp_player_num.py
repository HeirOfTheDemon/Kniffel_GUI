class tmpPlayer:
    def __init__(self):
        self.number_players = 2

    def addPlayer(self):
        self.number_players = min(self.number_players+1,8)

    def remPlayer(self):
        self.number_players = max(self.number_players-1,2)