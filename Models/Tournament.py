from Models.Game import Game
from Models.Organizer import organizer

class Tournament:
    
    """
    Búa til __init__ fall sem tekur inn nafn, byrjunardag, endadag,
    venue, contact person, contact_email, og contact_phone
    """
    def __init__(self, unique_name="", start_date="", end_date="", venue="", contact_person="", contact_email="", contact_phone=""):
        self.unique_name = unique_name
        self.start_date = start_date
        self.end_date = end_date
        self.venue = venue
        self.contact_person = contact_person
        self.contact_email = contact_email
        self.contact_phone = contact_phone


    "Skilar öllum upplýsingum mótsins í nýrri línu"

    def __str__(self, unique_name, start_date, end_date, venue, contact_person, contact_email, contact_phone):
        return f"{unique_name}:\n{start_date}:\n{end_date}:\n{venue}:\n{contact_person}:\n{contact_email}:\n{contact_phone}"
        
    def __repr__(self):
        return str(self)