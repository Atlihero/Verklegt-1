from logic_layer.LL_api import LL_API

class OrganizerUI:

    def createTournament(self):
        unique_name = input("Create a unique name for the tournament: ")
        
        while True:
            start_date = input("Select the start date of the tournament: ")
            try:
                start_date = LL_API.valid_start_date(start_date)
                break
            except ValueError as error:
                print(error)

        while True:
            end_date = input("Select the end date of the tournament: ")
            try:
                end_date = LL_API.valid_end_date(end_date)
                break
            except ValueError as error:
                print(error)

        venue = input("Enter the name of a venue (location) for the tournament: ")
        contact_person = input("Name the contact person for this tournament: ")
        
        while True:
            contact_email = input("What is the contact email for this tournament: ")
            try: 
                LL_API.valid_email(contact_email)
                break
            except ValueError as error:
                print(error)
        
        while True:
            contact_number = input("What is the contact phone for this tournament: ")
            try:
                LL_API.valid_phone(contact_number)
                break
            except ValueError as error:
                print(error)
        
        
        tournament_dict = {
            "unique_name": unique_name,
            "start_date": start_date,
            "end_date": end_date,
            "venue": venue,
            "contact_person": contact_person,
            "contact_email": contact_email,
            "contact_phone": contact_phone
            }
        api = LL_API()
        return api.create_new_tournaments(tournament_dict)