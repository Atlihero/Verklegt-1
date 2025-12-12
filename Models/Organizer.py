class Organizer():
    '''Class for organizer that gives his login and name'''
    
    def __init__(self, adminLogin: str ="", name: str =""):
        self.adminLogin = adminLogin
        self.name = name 

    
    def __str__(self):
        '''Return the information'''
        return (
        f"Login: {self.adminLogin}\n"
        f"Name : {self.name}"
        )


    def __repr__(self):
        return str(self)