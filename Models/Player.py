class Player:
    
    """
    Búa til __init__ fall sem tekur inn nafn, fæðingardag, heimili,
    email, viðurnefni(gamertag), og samfélagsmiðli
    """
    def __init__(self, name, dob, address, phone, email, handle, team, points=0):
        self.name = name
        self.dob = dob
        self.address = address
        self.phone = phone
        self.email = email
        self.handle = handle
        self.team = team
        self.points = int(points)

    #Skilar öllum upplýsingum leikmanns í nýrri línu
    def __str__(self):
        return (
            f"{self.name}:\n"
            f"{self.dob}:\n"
            f"{self.address}:\n"
            f"{self.phone}:\n"
            f"{self.email}:\n"
            f"{self.handle}:\n"
            f"{self.team}:\n"
            f"{self.points}"
        )
    def __repr__(self):
        return str(self)
        