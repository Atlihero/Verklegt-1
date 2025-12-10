from Models.Game import Game

class Result(Game):
    def __init__(self, score_a, score_b, winner):
        super().__init__()
        self.score_A = score_a
        self.score_B = score_b
        self.winner = winner

    def __str__(self):
        return f"{self.score_A}:\n{self.score_B}:\n{self.winner}"
