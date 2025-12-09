from Models import Player
from datetime import datetime
from data_layer.data_api import DataAPI
from data_layer.PlayerIO import PlayerIO

class LLPlayer():
    # because no names can be the same, doesn't add if they are the same
    #existing_handles = set() 
    #existing_handles = []

    def __init__(self):
        self.data = DataAPI()
        self.playerio = PlayerIO

    def get_all_players(self):
        return self.data.get_all_players()
    
    def get_player_publicViewer(self):
        return self.data.public_get_player()
    
    def get_player_statistics(self):
        return self.data.get_player_statistics()

    def validate_name(self, name: str) -> str:
        '''Checks if name is unique or missing a name'''
        # check if name is just empty, so just space or something
        name = name.strip()
        if not name:
            raise ValueError("Player name cannot be emtpy. Please enter a valid name.")
    
        return name


    def validate_dob(self, dob_str: str) -> datetime: 
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
        
    def validate_address(self, address: str) -> str:
        '''Checks if name is unique or missing a name'''
        # check if name is just empty, so just space or something
        address = address.strip()
        if not address:
            raise ValueError("Player's address name cannot be emtpy. Please enter a valid address.")
        
        return address
        
    def validate_phone(self, phone_number: int) -> int:
        '''Validates the players phone number, if not then 
          the user tries again.'''

		# number has to be exactly 7 digits long
        if len(phone_number) != 7 or not phone_number.isdigit():
            raise ValueError("Phone number must be exactly 7 digits long. Please try again")
        return phone_number
            

    def validate_email(self, player_email: str) -> str:
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

    def validate_handle(self, handle: str) -> str:
        '''Checks players handle. It checks if the username 
        is already in use and then asks for a new username since no two players 
        can have the same username '''
        handle = handle.strip()

        #if handle in LLPlayer.existing_handles:
        #    raise ValueError("This handle is already taken. Please try another one.")
        
        if not handle:
            raise ValueError("Player's handle name cannot be emtpy. Please enter a handle.")
        
        existing_usernames = self.data.get_all_players()
        existing_handles = [
            player["Handle"] 
            for player in existing_usernames
            if "Handle" in player
            ]
        
        if handle in existing_handles:
            raise ValueError("Handle is already in use, please choose another one.")

        return handle

		# if the handle is unique then its added to the list
        #LLPlayer.existing_handles.add(handle)
        #return handle
    
    def validate_link(self, link: str) -> str:
        if not link:
            return "" # user didn't add a link
        if not (link.startswith("http://") or link.startswith("https://")):
            raise ValueError("Link must start with 'http://' or 'https://'. Please try another link")
        return link
    
    #def create_player(self, name, dob_str, address, phone_number, player_email, player_handle, link):
    #    return Player.Player(name, dob_str, address, phone_number, player_email, player_handle, link)

    def create_player(self, player_obj: Player) -> Player:
    
        player_list = [ 
            player_obj.name,
            player_obj.dob,
            player_obj.address,
            player_obj.phone,
            player_obj.email,
            player_obj.handle,
            player_obj.link,
            player_obj.team,
            player_obj.points
        ]

        return self.playerio.create_new_player(player_list)
