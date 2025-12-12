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
        return(
         f"Score for team A  : {self.score_A}\n"
         f"Score for team B  : {self.score_B}\n"
         f"Winner            : {self.winner}"
         )


    def __repr__(self):
        return str(self)