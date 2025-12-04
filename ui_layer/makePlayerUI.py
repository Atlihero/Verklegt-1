from Models import Player
from datetime import datetime

class PlayerLL():

    def player_name(self):
        '''Asks user for full name'''
        
        name = input("Enter full name of player: ")
        return name
        
    def player_dob(self): 
        '''Asks the user for their date of birth and checks if the format
          fits the standards so the user can continue inputting the information.'''
        
        dob = input("Enter player date of birth (DD/MM/YYYY): ")
        try:
            # change string input to datetime
            entered_date = datetime.strptime(dob, "%d/%m/%Y")
            
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

                
    def player_address(self):
        '''Asks user for home address'''
        
        address = input("Enter player's home address: ")
        return address
        
    def player_phone(self):
        '''Asks the user for his phone number and checks if it is valid, if not then 
          the user tries again.'''
        
        phone_number = input("Enter player's phone number: ")
        
		# number has to be exactly 7 digits long
        if len(phone_number) == 7 and phone_number.isdigit():
            return f"{phone_number} is valid."
        elif len(phone_number) < 7 and phone_number.isdigit():
            print("Phone number must be 7 digits long. Please try")
            return PlayerLL.player_phone()
        else:
            print("Phone number must not be longer than 7 digits. Please try again")
            return PlayerLL.player_phone()

    def player_email(self):
        '''Asks the player for an email address and checks if it is valid so he can continue
          adding his information. Prints error messages when the input is not up to standards.'''

        player_email = input("Enter the player's email address: ")
        try:
            local_name, domain = player_email.split("@")
                
		# check if the inputted (innslegna) email has @ 
        except ValueError:
            if player_email.count("@") > 1:
                print("Email can only have 1 '@'. Please try again.")
            else:
                print("Email has to contain '@'. Please try again.")
            return PlayerLL.player_email()
        if not local_name:
            print("Local part (name) may not be empty. Please try again")
            return PlayerLL.player_email()
                
        # check if domain has a name and a dot, if not then invalid email address and user tries again
        domain_parts = domain.split(".")
        if len(domain_parts) < 2 or not domain_parts[0] or not domain_parts[1]:
                print("Domain must have a name and a valid ending. Please try again.")
                return PlayerLL.player_email()
                
        # check if end of domain has valid ending after the dot
        ending = domain.split(".")[-1]
        if len(ending) < 2 or len(ending) > 3 or not ending.isalpha():
            print("The email must contain a valid ending. Please try again.")
            return PlayerLL.player_email()
        
        return f"{player_email} is a valid email"

    def player_handle(self):
        '''Asks user for a username (handle) to use for the games. It cecks if the username 
        is already in use and then asks for a new username since no two players 
        can have the same username '''
        #move empty list to the ouside of function
        handle = input("Enter player's handle: ")
        existing_handles: list = []
        
        if handle in existing_handles:
            print("This handle is already taken. Please try another one.")
            return PlayerLL.player_handle()
        
		# if the handle is unique then its added to the list
        existing_handles.append(handle)
        print("Handle has been added to the list")
        return handle