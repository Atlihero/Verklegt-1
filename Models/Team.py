from Models.Player import Player

class Team:
    def __init__(self, name, captain, players, asciiLogo):
        self.name = name
        self.captain = captain
        self.players = players
        self.asciiLogo = asciiLogo
    
    def __str__(self, name, captain, players, asciiLogo):
        return f"{name}:\n{captain}:\n{players}:\n{asciiLogo}"
        
    


        