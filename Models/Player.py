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

    "Skilar öllum upplýsingum leikmanns mí nýrri línu"
    def __str__(self, name, dob, address, email, handle, link):
        return f"{name}:\n{dob}:\n{address}:\n{email}:\n{handle}:\n{link}"
        