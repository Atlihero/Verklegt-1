from Models.Organizer import Organizer

class Tournament(Organizer):
    '''Class that takes in information about the tournament'''
    def __init__(self, unique_name, start_date, end_date, venue, contact_person, contact_email, contact_phone):
        self.unique_name = unique_name
        self.start_date = start_date
        self.end_date = end_date
        self.venue = venue
        self.contact_person = contact_person
        self.contact_email = contact_email
        self.contact_phone = contact_phone

    
    def __str__(self):
        '''Return the information'''
        return (
        f"Name                  : {self.unique_name}\n"
        f"Start date            : {self.start_date}\n"
        f"End date              : {self.end_date}\n"
        f"Location              : {self.venue}\n"
        f"Contact person        : {self.contact_person}\n"
        f"Contact person email  : {self.contact_email}\n"
        f"Contact person phone  : {self.contact_phone}"
        )

    
    def __repr__(self):
        return str(self)
