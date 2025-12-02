from Models.Player import Player

class Team:
    "Klasi fyrir nafn, kaftein, leikmenn og ASCII logo á lið "
    def __init__(self, name, captain, players, asciiLogo):
        self.name = name
        self.captain = captain
        self.players = players
        self.asciiLogo = asciiLogo
    
    "Strengur sem skilar þeim úpllýsingum í nýjum línum"
    def __str__(self, name, captain, players, asciiLogo):
        return f"{name}:\n{captain}:\n{players}:\n{asciiLogo}"
