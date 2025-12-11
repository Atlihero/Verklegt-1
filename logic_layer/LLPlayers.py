from Models.Player import Player
from datetime import datetime
from data_layer.data_api import DataAPI
from data_layer.PlayerIO import PlayerIO

class LLPlayer():

    def __init__(self):
        self.data = DataAPI()
        self.playerio = PlayerIO


    def get_all_players(self):
        '''Gets the players from the csv file'''
        
        return self.data.get_all_players()
    
    
    def get_player_public_viewer(self):
        '''Gets the players for the public viewers'''
       
        return self.data.public_get_player()

	
    def validate_name(self, name: str) -> str:
        '''Checks if name input is missing'''
        
        name = name.strip()
        if not name: # Check if empty
            raise ValueError("Player name cannot be emtpy. Please enter a valid name.")
    
        return name


    def validate_dob(self, dob_str: str) -> datetime: 
        '''Checks player's date of birth and if the format fits the 
        standards, then the user can continue inputting the information.'''
        
        try:
            # change string input to datetime
            dob = datetime.strptime(dob_str, "%d/%m/%Y")
            
			# check if inputted date is in the future, then invalid
            if dob > datetime.now():
                raise ValueError("Please enter a valid date.")
            return dob
        except ValueError:
            raise ValueError ("Invalid date. Use DD/MM/YYYY")
        

    def validate_address(self, address: str) -> str:
        '''Checks if address input is empty'''
        
        address = address.strip()
        if not address: # Check if empty
            raise ValueError("Player's address name cannot be emtpy. Please enter a valid address.")
        
        return address
        

    def validate_phone(self, phone_number: str) -> str:
        '''Validates the players phone number, if invalid then 
          the user tries again.'''
        
        phone_number = phone_number.strip()
        if not phone_number: # Check if empty
            raise ValueError("Player's phone number cannot be emtpy. Please enter a phone number.")
        
		# Number has to be exactly 7 digits long, the country code is already inputted
        if len(phone_number) != 10 or not phone_number.isdigit():
            raise ValueError("Phone number must be exactly 7 digits long. Please acknowledge that the coutnry code is already inputted.")
        
        existing_phone_number: list[Player] = self.data.get_all_players()
    
        for number in existing_phone_number:
            if number.phone == phone_number:
                raise ValueError("Phone number is already in use. Please choose another one.")
			
        return phone_number
            

    def validate_email(self, player_email: str) -> str:
        '''Checks players email address and if it is valid then he can contiue.
           If email is invalid the user tries again.'''
        
        try:
            local_name, domain = player_email.split("@")
                
		# Check if the inputted email has @ 
        except ValueError:
                raise ValueError("Email must contain a single '@'. Please try again.")
            
        if not local_name:
            raise ValueError("Local part (name) may not be empty. Please try again")
                
        # Check if the domain has a name and a dot, if not then the email address is invalid and the user tries again
        domain_parts = domain.split(".")
        if len(domain_parts) < 2 or not all(domain_parts):
            raise ValueError("Domain must have a name and a valid ending. Please try again.")
                 
        # Check if end of domain has valid ending after the dot
        ending = domain_parts[-1]
        if len(ending) < 2 or len(ending) > 3 or not ending.isalpha():
            raise ValueError("The email must contain a valid ending. Either 2 or 3 letters. Please try again.")
		
        existing_email: list[Player] = self.data.get_all_players()
        existing_emails = []
        for emails in existing_email:
            if emails:
                existing_emails.append(emails.email)

        if player_email in existing_emails:
                raise ValueError("Email is already in use. Please choose another one.")

        return player_email


    def validate_handle(self, handle: str) -> str:
        '''Checks if the username is already in use. No two users can have the same username '''
        
        handle = handle.strip()
        if not handle: # Check if empty
            raise ValueError("Player's handle name cannot be emtpy. Please enter a handle.")

        existing_usernames: list[Player] = self.data.get_all_players()
        existing_handles = []
        for player in existing_usernames: 
            if player:
                existing_handles.append(player.handle)
        
        if handle in existing_handles: # Checking if the handle is already in use
            raise ValueError("Handle is already in use, please choose another one.")

        return handle

    
    def validate_link(self, link: str) -> str:
        '''Checks if the link is a valid link'''
        if not link:
            return "" # User didn't add a link
        if not (link.startswith("http://") or link.startswith("https://")):
            raise ValueError("Link must start with 'http://' or 'https://'. Please try another link")
        return link
    

    def create_player(self, player_obj: Player) -> Player:
        '''Creates the player and adds it to the csv file.'''
        player_list = [ 
            player_obj.name,
            player_obj.dob,
            player_obj.address,
            player_obj.phone,
            player_obj.email,
            player_obj.handle,
            player_obj.team,
            player_obj.link
        ]

        return self.playerio.create_new_player(player_list)
