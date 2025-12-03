class Player:
    
    """
    Búa til __init__ fall sem tekur inn nafn, fæðingardag, heimili,
    email, viðurnefni(gamertag), og link að samfélagsmiðli
    """
    def __init__(self, name="", dob="", address="", email="", handle="", link=""):
        self.name = name
        self.dob = dob
        self.address = address
        self.email = email
        self.handle = handle
        self.link = link

    #Skilar öllum upplýsingum leikmanns í nýrri línu
    def __str__(self):
        return f"{self.name}:\n{self.dob}:\n{self.address}:\n{self.email}:\n{self.handle}:\n{self.link}"
    
    def __repr__(self):
        return str(self)
        