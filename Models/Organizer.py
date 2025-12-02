class Organizer():
    def __init__(self, adminLogin: str ="", name: str =""):
        self.adminLogin = adminLogin
        self.name = name 
    
    def __str__(self):

        return f"Organizer(adminLogin='{self.adminLogin}', name='{self.name}')"