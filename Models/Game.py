from Models.Team import Team
from Models.Organizer import Organizer

class Game:
    def __init__(self, date, roundnumber, ):
        self.date = date
        self.roundenumber = roundnumber
        
    def __str__(self, date, roundnum):
        return