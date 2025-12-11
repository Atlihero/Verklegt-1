from dataclasses import dataclass #TODO: this is not being used
from datetime import date

class Player:
    
    """
    Búa til __init__ fall sem tekur inn nafn, fæðingardag, heimili,
    email, viðurnefni(gamertag), og link að samfélagsmiðli
    """
    def __init__(self, name, dob, phone, address, email, handle, link, team=None):        
        self.name: str = name
        self.dob: date = dob
        self.address: int = address
        self.phone: str = phone
        self.email: str = email
        self.handle: str = handle
        self.team: str = team
        self.link: str = link

    def __str__(self):
        dob_str = self.dob.strftime("%d/%m/%Y") if hasattr(self.dob, "strftime") else self.dob
        
        return (
        f"Name    : {self.name}\n"
        f"DOB     : {dob_str}\n"
        f"Address : {self.address}\n"
        f"Phone   : {self.phone}\n" 
        f"Email   : {self.email}\n"
        f"Handle  : {self.handle}\n"
        f"Team    : {self.team}\n"
        f"Link    : {self.link}"
        )
    def __repr__(self):
        return str(self)
        
