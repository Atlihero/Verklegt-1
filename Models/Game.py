

class Game:
    def __init__(self, team1, team2, result= None):
        self.team1 = team1
        self.team2 = team2
        self.result = result


    def __str__(self):
        return f"{self.team1}:\n{self.team2}:\n{self.result}"
    
    def __repr__(self):
        return str(self)