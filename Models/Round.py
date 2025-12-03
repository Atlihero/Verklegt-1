from Models.Tournament import Tournament #importa tournament klasan

#Klasi fyrir round á tournamenti sem segja númer hvað roundið er líka byrjunar og endatíma á roundinu
class Round(Tournament):
    def __init__(self, number, startTime, endTime):
        self.number = number
        self.startTime = startTime
        self.endTime = endTime


    def __str__(self):
        #Skilar niðurstöðunum í nýjum línum
        return f"{self.name}:\n{self.number}:\n{self.startTime}:\n{self.endTime}"
    
    #Konni sagði að það væri sniðugt að hafa svona
    def __repr__(self):
        return str(self)
    