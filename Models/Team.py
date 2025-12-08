class Team:
    #Klasi fyrir nafn, kaftein, leikmenn og ASCII logo á lið
    def __init__(self, name, captain, asciiLogo, wins: int = 0, points: int = 0):
        self.name = name
        self.captain = captain
        self.asciiLogo = asciiLogo
        self.wins = wins
        self.points = points
    
    #Strengur sem skilar þeim úpllýsingum í nýjum línum
    def __str__(self):
        return f"{self.name}:\n{self.captain}:\n{self.asciiLogo}:\n{self.wins}:\n{self.points}"

    def __repr__(self):
        return str(self)