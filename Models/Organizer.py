#Klasi fyrir organizerinn sem gefur login hjá honum og nafn
class Organizer():
    def __init__(self, adminLogin: str ="", name: str =""):
        self.adminLogin = adminLogin
        self.name = name 
    
    #skila upllýsingunum
    def __str__(self):
        return f"Organizer(adminLogin='{self.adminLogin}', name='{self.name}')"