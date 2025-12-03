from Models.Player import Player

class Team(Player):
    #Klasi fyrir nafn, kaftein, leikmenn og ASCII logo á lið
    def __init__(self, name, captain, asciiLogo):
        self.name = name
        self.captain = captain
        self.asciiLogo = asciiLogo
    
    #Strengur sem skilar þeim úpllýsingum í nýjum línum
    def __str__(self, name, captain, asciiLogo):
        return f"{name}:\n{captain}:\n{asciiLogo}"

    def __repr__(self):
        return str(self)