from Models.Round import Round #importar round klasanum

#klasi fyrir leiki sem segja hvenær þeir eru og að passa að það séu slétttölu
class Game(Round):
    def __init__(self, date, roundnumber):
        super().__init__()
        self.date = date
        self.roundenumber = roundnumber

    #skilar þeim upplýsingum    
    def __str__(self):
        return f"{self.date}:\n{self.roundenumber}"
    
    def __repr__(self):
        return str(self)