from datetime import datetime
from data_layer.data_api import DataAPI
from data_layer.PlayerIO import PlayerIO

class LLOrganizer():
    
    def __init__(self):
        self.dapi = DataAPI()
        self.playerio = PlayerIO()
    

    def tournament_name(self, name: str) -> str:
        '''Checks if name is unique or missing a name'''
        # check if name is just empty, so just space or something
        name = name.strip()
        if not name:
            raise ValueError("Tournament name cannot be emtpy. Please enter a valid name.")
        
        existing_tournament_names = self.dapi.get_all_tournaments()
        existing_name = []
        for row in existing_tournament_names:
            if row: #check if row is not empty, to prevent error
                existing_name.append(row[0])

        if name in existing_name:
            raise ValueError("Name already exists, please choose another one.")

        return name
       

    def choose_start_date(self, start_date: str) -> datetime:
        '''Check if the start_date for a tournament is a valid date'''
        try:
            # change string input to datetime
            start_date = datetime.strptime(start_date, "%d/%m/%Y")
            
			# check if inputted date is in the future, then not valid
            if start_date < datetime.now():
                raise ValueError("Date has to be in the future. Please enter a valid date.")
            return start_date
        except ValueError:
            raise ValueError ("Invalid date. Use DD/MM/YYYY")

    
    def choose_end_date(self, end_date, start_date) -> datetime:
        '''Check if the end date for a tournament is a valid date'''
        try:
            # change string input to datetime
            end_date = datetime.strptime(end_date, "%d/%m/%Y")
            
			# check if inputted date is in the future, then not valid
            if end_date < start_date: #LLOrganizer.choose_start_date(start_date):
                raise ValueError("Date has to be after the start date. Please enter a valid date.")
            return end_date
        except ValueError:
            raise ValueError ("Invalid date. Use DD/MM/YYYY")
    
    def organizer_player_info(self):
        """Allows the organizer to see all the players information"""
        all_players = self.playerio.get_players()
        return all_players