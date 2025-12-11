from Models.Round import Round

class Game(Round):
    '''Class for games that says when they are and make sure 
    that there are even numbered amount of teams'''
   
    def __init__(self, date, round):
        super().__init__()
        self.date = date
        self.round = round


    def __str__(self):
        '''Return the information'''
        return f"{self.date}:\n{self.round}"

    
    def __repr__(self):
        return str(self)
