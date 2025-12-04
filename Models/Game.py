from Models.Round import Round #importar round klasanum

#klasi fyrir leiki sem segja hvenær þeir eru og að passa að það séu slétttölu
class Game(Round):
    def __init__(self, date, round):
        super().__init__()
        self.date = date
        self.round = round


    def __str__(self):
        return f"{self.date}:\n{self.round}"
    
    def __repr__(self):
        return str(self)