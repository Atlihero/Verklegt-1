from dataclasses import dataclass
from datetime import date

class Player:
    
    """
    Búa til __init__ fall sem tekur inn nafn, fæðingardag, heimili,
    email, viðurnefni(gamertag), og link að samfélagsmiðli
    """
    def __init__(self, name="", dob="", phone="", address="", email="", handle="", link=""):
        self.name: str = name
        self.dob: date = dob
        self.phone: int = phone
        self.address: str = address
        self.email: str = email
        self.handle: str = handle
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
        f"Link    : {self.link}"
        )
    def __repr__(self):
        return str(self)
        