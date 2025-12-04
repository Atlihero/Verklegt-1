

class Round:
    def __init__(self, name, games=None):
        self.name = name
        self.games = games if games is not None else []

    def __str__(self):
        return f"{self.name}:\n{self.games}"
    
    def __repr__(self):
        return str(self)
    