from Models.Tournament import Tournament
from datetime import datetime

class Round():
    def __init__(self, name, number, startTime, endTime):
        self.name = name
        self.number = number
        self.startTime = startTime
        self.endTime = endTime

    def __str__(self, name, number, startTime, endTime):
        return f"{name}:\n{number}:\n{startTime}:\n{endTime}"
    
    def __repr__(self):
        return str(self)
    