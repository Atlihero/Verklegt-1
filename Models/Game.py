from Models.Round import Round
from Models.Tournament import Tournament

class Game:
    def __init__(self, date, roundnumber):
        self.date = date
        self.roundenumber = roundnumber
        
    def __str__(self):
        return f"{self.date}\n{self.roundenumber}"
    
    def __repr__(self):
        return str(self)