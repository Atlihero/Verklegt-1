from Models import Player
from datetime import datetime
from ui_layer import makePlayerUI

class PlayerLL():

    def player_dob(self): 
        '''Checks players date of birth and if the format fits the 
        standards, then the user can continue inputting the information.'''

        try:
            # change string input to datetime
            entered_date = datetime.strptime(makePlayerUI.dob, "%d/%m/%Y")
            
			# check if inputted date is in the future, then not valid
            if entered_date > datetime.now():
                print("Please enter a valid date.")
                return PlayerLL.player_dob()
            else:
                day = entered_date.day
                month = entered_date.month
                year = entered_date.year
                print(f"{day}/{month}/{year}")
        
		# lets the user try again if he inputted wrong   
        except ValueError:
            print("Invalid date. Try again using DD/MM/YYYY.")
            return PlayerLL.player_dob()

        
    def player_phone(self):
        '''Validates the players phone number, if not then 
          the user tries again.'''

		# number has to be exactly 7 digits long
        if len(phone_number) == 7 and phone_number.isdigit():
            return f"{phone_number} is valid."
        elif len(phone_number) < 7 and phone_number.isdigit():
            raise("Phone number must be 7 digits long. Please try")
            
        else:
            raise("Phone number must not be longer than 7 digits. Please try again")
            

    def player_email(self):
        '''Checks players email address and if it is valid then he can contiue.
           Raises error messages when the input is not up to standards.'''

        try:
            local_name, domain = player_email.split("@")
                
		# check if the inputted (innslegna) email has @ 
        except ValueError:
            if player_email.count("@") > 1:
                raise("Email can only have 1 '@'. Please try again.")
            else:
                raise("Email has to contain '@'. Please try again.")
            
        if not local_name:
            raise("Local part (name) may not be empty. Please try again")
            
                
        # check if domain has a name and a dot, if not then invalid email address and user tries again
        domain_parts = domain.split(".")
        if len(domain_parts) < 2 or not domain_parts[0] or not domain_parts[1]:
                raise("Domain must have a name and a valid ending. Please try again.")
                
        # check if end of domain has valid ending after the dot
        ending = domain.split(".")[-1]
        if len(ending) < 2 or len(ending) > 3 or not ending.isalpha():
            raise("The email must contain a valid ending. Please try again.")
            
        
        return f"{player_email} is a valid email"

    def player_handle(self):
        '''Checks players handle. It checks if the username 
        is already in use and then asks for a new username since no two players 
        can have the same username '''
        #move empty list to the ouside of function????
        existing_handles: list = []
        
        if handle in existing_handles:
            raise("This handle is already taken. Please try another one.")
        
		# if the handle is unique then its added to the list
        existing_handles.append(handle)
        raise("Handle has been added to the list")
        