class Team:
    '''Class for information about each team'''
    def __init__(self, name, captain, asciiLogo, wins: int = 0, points: int = 0):
        self.name = name
        self.captain = captain
        self.asciiLogo = asciiLogo
        self.wins = wins
        self.points = points

    
    def __str__(self):
        '''Return the information'''
        return (
        f"Name      : {self.name}\n"
        f"Captain   : {self.captain}\n"
        f"AsciiLogo : {self.asciiLogo}"
        )

    
    def __repr__(self):
        return str(self)
