class Organizer():

# Býr til nýjan skipuleggjanda með innskráningu stjórnanda og nafni 
    def __init__(self, adminLogin: str ="", name: str =""):
        self.adminLogin = adminLogin
        self.name = name 
#Skilar lesanlegri strengjaframsetningu fyrir hlutinn  
    def __str__(self):

        return f"Organizer(adminLogin='{self.adminLogin}', name='{self.name}')"