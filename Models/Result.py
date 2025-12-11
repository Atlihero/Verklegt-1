from Models.Game import Game

class Result(Game):
    '''Class that keeps track of the results of each round'''
    def __init__(self, score_A, score_B, winner):
        super().__init__()
        self.score_A = score_A
        self.score_B = score_B
        self.winner = winner

    
    def __str__(self):
        '''Return the information'''
        return f"{self.score_A}:\n{self.score_B}:\n{self.winner}"
