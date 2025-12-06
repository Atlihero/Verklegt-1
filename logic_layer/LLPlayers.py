from Models import Player
from datetime import datetime

class LLPlayer():
    # because no names can be the same, doesn't add to set if they are the same
    existing_handles = set() 

    def validate_dob(dob_str: str) -> datetime: 
        '''Checks players date of birth and if the format fits the 
        standards, then the user can continue inputting the information.'''

        try:
    # change string input to datetime, it cannot be a day or month that does not exist
            dob = datetime.strptime(dob_str, "%d/%m/%Y")
            
			# check if inputted date is in the future, then not valid
            if dob > datetime.now():
                raise ValueError("Please enter a valid date using DD/MM/YYYY.")
            return dob
        except ValueError:
            raise ValueError ("Invalid date. Use DD/MM/YYYY")
        

    def validate_phone(phone_number: int) -> int:
        '''Validates the players phone number, if not valid then 
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
                raise ValueError("Email must contain a '@'. Please try again.")
            
        if not local_name:
            raise ValueError("Local part (before '@') may not be empty. Please try again")
            
                
    # check if domain has a name and a dot, if not then invalid email address
        domain_parts = domain.split(".")
        if len(domain_parts) < 2 or not all(domain_parts):
            raise ValueError("Domain must have a name and a valid ending. Please try again.")
                 
        # check if end of domain has valid ending after the dot
        # has to be either 2 or 3 letters
        ending = domain_parts[-1]
        if len(ending) < 2 or len(ending) > 3 or not ending.isalpha():
            raise ValueError("The email must contain a valid ending. Please try again.")
            
        return player_email


    def validate_handle(handle: str) -> str:
        '''Checks players handle. It checks if the handle 
        is already in use and then asks for a new handle since no two players 
        can have the same username '''
        
        if handle in LLPlayer.existing_handles:
            raise ValueError("This handle is already taken. Please try another one.")
        
		# if the handle is unique then it it added to the player
        LLPlayer.existing_handles.add(handle)
        return handle
    

    def validate_link(link: str) -> str:
        if not link:
            return "" # empty if the user didn't add a link
        if not (link.startswith("http://") or link.startswith("https://")):
            raise ValueError("Link must start with 'http://' or 'https://'. Please try another link")
        return link
    

    def create_player(name, dob_str, address, phone_number, player_email, player_handle, link, team = "", points = 0):
        return Player.Player(name, dob_str, address, phone_number, player_email, player_handle, team, points, link)