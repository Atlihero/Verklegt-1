from Models.Game import Game

class Result(Game):
    #Klasi fyrir score_A, score_B og winner
    def __init__(self, score_A, score_B, winner):
        self.score_A = score_A
        self.score_B = score_B
        self.winner = winner
    
    #Strengur sem skilar þeim úpllýsingum í nýjum línum
    def __str__(self):
        return f"{self.score_A}:\n{self.score_B}:\n{self.winner}"

    def __repr__(self):
        return str(self)