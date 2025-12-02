from Models.Game import Game

class Result:
    
    """
    Búa til __init__ fall sem tekur inn score_A, score_B, og winner
    """
    def __init__(self, score_A="", score_B="", winner=""):
        self.score_A = score_A
        self.score_B = score_B
        self.winner = winner


    "Skilar öllum upplýsingum niðurstaðana (results) í nýrri línu"

    def __str__(self, score_A, score_B, winner):
        return f"{score_A}:\n{score_B}:\n{winner}"
        
    def __repr__(self):
        return str(self)