from Models.Tournament import Tournament

class Round(Tournament):
    '''Class for each round of the tournament that number what
    the round is and when it starts and ends'''
    def __init__(self, number, startTime, endTime):
        self.number = number
        self.startTime = startTime
        self.endTime = endTime


    def __str__(self):
        '''Returns the information'''
        return f"{self.name}:\n{self.number}:\n{self.startTime}:\n{self.endTime}"

    
    def __repr__(self):
        return str(self)
    
