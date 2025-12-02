class Player:
    
    def __init__(self, name="", dob="", address="", email="", handle="", link=""):
        self.name = name
        self.dob = dob
        self.address = address
        self.email = email
        self.handle = handle
        self.link = link

    def __str__(self, name, dob, address, email, handle, link):
        return f"{name}:\n\t{dob}:\n\t{address}:\n\t{email}:\n\t{handle}:\n\t{link}"
        
    def name():
        pass
        