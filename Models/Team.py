class Team:
    '''Class for information about each team'''
    def __init__(self, name, captain, asciiLogo):
        self.name = name
        self.captain = captain
        self.asciiLogo = asciiLogo

    
    def __str__(self):
        '''Return the information'''
        return (
        f"Name      : {self.name}\n"
        f"Captain   : {self.captain}\n"
        f"AsciiLogo : {self.asciiLogo}"
        )

    
    def __repr__(self):
        return str(self)
