class Team:
    #Klasi fyrir nafn, kaftein, leikmenn og ASCII logo á lið
    def __init__(self, name, captain, asciiLogo):
        self.name = name
        self.captain = captain
        self.asciiLogo = asciiLogo
    
    #Strengur sem skilar þeim úpllýsingum í nýjum línum
    def __str__(self):
        return (
        f"Name      : {self.name}\n"
        f"Captain   : {self.captain}\n"
        f"AsciiLogo : {self.asciiLogo}"
        )

    def __repr__(self):
        return str(self)