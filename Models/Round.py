from Models.Tournament import Tournament #importa tournament klasan
from datetime import datetime #importa tímanum

#Klasi fyrir round á tournamenti sem segja númer hvað roundið er líka byrjunar og endatíma á roundinu
class Round():
    def __init__(self, number, startTime, endTime):
        self.number = number
        self.startTime = startTime
        self.endTime = endTime


    def __str__(self, name, number, startTime, endTime):
        #Skilar niðurstöðunum í nýjum línum
        return f"{name}:\n{number}:\n{startTime}:\n{endTime}"
    
    #Konni sagði að það væri sniðugt að hafa svona
    def __repr__(self):
        return str(self)
    