from logic_layer.LL_api import LL_API
from Models.Tournament import Tournament

class OrganizerUI():

    def createTournament(self):
        lapi = LL_API()
    
        while True:
            unique_name = input("Create a unique name for the tournament: ")
            try:
                unique_name = lapi.valid_tournament_name(unique_name)
                break
            except ValueError as error:
                print(error)

        while True:
            start_date = input("Select the start date of the tournament: ")
            try:
                start_date = lapi.valid_start_date(start_date)
                break
            except ValueError as error:
                print(error)

        while True:
            end_date = input("Select the end date of the tournament: ")
            try:
                end_date = lapi.valid_end_date(end_date, start_date)
                break
            except ValueError as error:
                print(error)

        venue = input("Enter the name of a venue (location) for the tournament: ")
        contact_person = input("Name the contact person for this tournament: ")
        
        while True:
            contact_email = input("What is the contact email for this tournament: ")
            try: 
                lapi.valid_email(contact_email)
                break
            except ValueError as error:
                print(error)
        
        while True:
            contact_phone = input("What is the contact phone for this tournament: ")
            try:
                lapi.valid_phone(contact_phone)
                break
            except ValueError as error:
                print(error)
        
        
    # have it as an object not an dict.
        tournament_obj = Tournament( 
            unique_name=unique_name,
            start_date=start_date,
            end_date=end_date,
            venue=venue,
            contact_person=contact_person,
            contact_email=contact_email,
            contact_phone=contact_phone
        )

        return lapi.create_new_tournament(tournament_obj)
