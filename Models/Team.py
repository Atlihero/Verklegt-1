class Team:
    #Klasi fyrir nafn, kaftein, leikmenn og ASCII logo á lið
    def __init__(self, name, captain, asciilogo):
        self.name = name
        self.captain = captain
        self.asciilogo = asciilogo
        self.members = []
    
    #Strengur sem skilar þeim upplýsingum í nýjum línum
    def __str__(self):
        return f"{self.name}:\n{self.captain}"

    def __repr__(self):
        return str(self)