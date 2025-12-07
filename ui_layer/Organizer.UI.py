from logic_layer.LL_api import LL_API()
from Models.Tournament import Tournament

class OrganizerUI:

    def createTournament(self):
        unique_name = input("Create a unique name for the tournament: ")
        start_date = input("Select the start date of the tournament: ")
        end_date = input("Select end date for the tournament: ")
        venue = input("Select the venue for the tournament: ")
        contact_person = input("Name the contact person for this tournament: ")
        contact_email = input("What is the contact email for this tournamnet: ")
        contact_phone = input("What is the contact phone for this tournament: ")

        t = Tournament(unique_name, start_date, end_date, venue, contact_person, contact_email, contact_phone)

        api = LL_API()
        
        return api.create_new_tournaments()

