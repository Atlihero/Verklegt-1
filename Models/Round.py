from Models.Tournament import Tournament

class Round(Tournament):
    '''Class for each round of the tournament that number what
    the round is and when it starts and ends'''
    def __init__(self, number, startTime, endTime):
        self.number = number
        self.start_time = startTime
        self.end_time = endTime

    
    def __str__(self):
        '''Return the information'''
        return (
        f"Number: {self.number}\n"
        f"Start Time: {self.start_time}\n"
        f"End Time: {self.end_time}"
        )

    
    def __repr__(self):
        return str(self)
    
    
