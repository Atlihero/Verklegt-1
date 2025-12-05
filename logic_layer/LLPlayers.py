from Models.Player import Player
from datetime import datetime
from data_layer.data_api import DataAPI

class LLPlayer:
    # because no names can be the same, doesn't add if they are the same
    existing_handles = set() 

    
    def get_all_players(self):
        data = DataAPI()
        return data.get_all_players()
    
    def get_player_publicViewer(self):
        data = DataAPI()
        return data.public_get_player()
    
    def get_player_statistics(self):
        return super().get_player_statistics()

    def validate_dob(dob_str: str) -> datetime: 
        '''Checks players date of birth and if the format fits the 
        standards, then the user can continue inputting the information.'''

        try:
            # change string input to datetime
            dob = datetime.strptime(dob_str, "%d/%m/%Y")
            
			# check if inputted date is in the future, then not valid
            if dob > datetime.now():
                raise ValueError("Please enter a valid date.")
            return dob
        except ValueError:
            raise ValueError ("Invalid date. Use DD/MM/YYYY")
        
    def validate_phone(phone_number: int) -> int:
        '''Validates the players phone number, if not then 
          the user tries again.'''

		# number has to be exactly 7 digits long
        if len(phone_number) != 7 or not phone_number.isdigit():
            raise ValueError("Phone number must be exactly 7 digits long. Please try again")
        return phone_number
            

    def validate_email(player_email: str) -> str:
        '''Checks players email address and if it is valid then he can contiue.
           Raises error messages when the input is not up to standards.'''

        try:
            local_name, domain = player_email.split("@")
                
		# check if the inputted (innslegna) email has @ 
        except ValueError:
                raise ValueError("Email must contain a single '@'. Please try again.")
            
        if not local_name:
            raise ValueError("Local part (name) may not be empty. Please try again")
            
                
        # check if domain has a name and a dot, if not then invalid email address and user tries again
        domain_parts = domain.split(".")
        if len(domain_parts) < 2 or not all(domain_parts):
                raise ValueError("Domain must have a name and a valid ending. Please try again.")
                 
        # check if end of domain has valid ending after the dot
        ending = domain_parts[-1]
        if len(ending) < 2 or len(ending) > 3 or not ending.isalpha():
            raise ValueError("The email must contain a valid ending. Please try again.")
            
        
        return player_email

    def validate_handle(handle: str) -> str:
        '''Checks players handle. It checks if the username 
        is already in use and then asks for a new username since no two players 
        can have the same username '''
        
        if handle in LLPlayer.existing_handles:
            raise ValueError("This handle is already taken. Please try another one.")
        
		# if the handle is unique then its added to the list
        LLPlayer.existing_handles.add(handle)
        return handle
    
    def validate_link(link: str) -> str:
        if not link:
            return "" # user didn't add a link
        if not (link.startswith("http://") or link.startswith("https://")):
            raise ValueError("Link must start with 'http://' or 'https://'. Please try another link")
        return link
    
    def create_player(name, dob_str, address, phone_number, player_email, player_handle, link):
        return Player.Player(name, dob_str, address, phone_number, player_email, player_handle, link)
