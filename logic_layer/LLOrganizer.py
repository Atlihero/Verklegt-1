from datetime import datetime
from data_layer.data_api import DataAPI
from data_layer.PlayerIO import PlayerIO

class LLOrganizer():
    
    def __init__(self):
        self.dapi = DataAPI()
        self.playerio = PlayerIO()
    

    def tournament_name(self, name: str) -> str:
        '''Checks if name is unique or missing a name'''
        
        name = name.strip()
        if not name: # Check for empty inputs
            raise ValueError("Tournament name cannot be emtpy. Please enter a valid name.")
        
        # Get all tournament names from the csv file
        existing_tournament_names = self.dapi.get_all_tournaments()
        existing_name = [row[0] for row in existing_tournament_names if row]
        if name in existing_name: # Checking if the name is unique
            raise ValueError("Name already exists, please choose another one.")

        return name
       

    def choose_start_date(self, start_date: str) -> datetime:
        '''Check if the start date for a tournament is a valid date'''
        try:
            # Change string input to datetime
            start_date = datetime.strptime(start_date, "%d/%m/%Y")
            
			# Check if inputted date is in the future, if not in the future then invalid date
            if start_date < datetime.now():
                raise ValueError("Date has to be in the future. Please enter a valid date.")
            return start_date
        except ValueError: # If the formatting is wrong
            raise ValueError ("Invalid date. Use DD/MM/YYYY")

    
    def choose_end_date(self, end_date, start_date) -> datetime:
        '''Check if the end date for a tournament is a valid date'''
        try:
            # Change string input to datetime
            end_date = datetime.strptime(end_date, "%d/%m/%Y")
            
			# Check if inputted end date is after the start date
            if end_date < start_date:
                raise ValueError("Date has to be after the start date. Please enter a valid date.")
            return end_date
        except ValueError:
            raise ValueError ("Invalid date. Use DD/MM/YYYY")
    

    def tournament_location(self, location: str) -> str:
        '''Checks if name is unique or missing a name'''

        location = location.strip()
        if not location: # Check for empty input
            raise ValueError("Tournament location cannot be emtpy. Please enter a location.")

        return location
    

    def tournament_contact_name(self, contact_name: str) -> str:
        '''Checks if name is unique or missing a name'''

        contact_name = contact_name.strip()
        if not contact_name: # Check for empty input
            raise ValueError("Contact name cannot be emtpy. Please enter a contact person.")
        return contact_name
    

    def organizer_player_info(self):
        """Allows the organizer to see information on all the players"""
        all_players = self.playerio.get_players()
        return all_players