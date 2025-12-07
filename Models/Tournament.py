"""
    Búa til __init__ fall sem tekur inn unique nafn, byrjunardag, endadag,
    staðsetning, contact person, contact email og contact phone 
"""

class Tournament():
    def __init__(self, unique_name, start_date, end_date, venue, contact_person, contact_email, contact_phone):
        self.unique_name = unique_name
        self.start_date = start_date
        self.end_date = end_date
        self.venue = venue
        self.contact_person = contact_person
        self.contact_email = contact_email
        self.contact_phone = contact_phone
    


    def __str__(self):
            return (
            f"Tournament: {self.unique_name}\n"
            f"Start: {self.start_date}\n"
            f"End: {self.end_date}\n"
            f"Venue: {self.venue}\n"
            f"Contact: {self.contact_person}\n"
            f"Email: {self.contact_email}\n"
            f"Phone: {self.contact_phone}"
        )
    
    def __repr__(self):
        return str(self)