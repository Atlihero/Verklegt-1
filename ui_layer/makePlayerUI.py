from Models import Player
from datetime import datetime
from logic_layer import LLPlayers


def get_player_info():
    
        
        name = input("Enter full name of player: ")
           
        try:
            dob_str = input("Enter player date of birth (DD/MM/YYYY): ")
            dob = LLPlayers.validate_dob(dob_str)
        except ValueError as error:
            print(error)
            
        
        address = input("Enter player's home address: ")


        try:
            phone_number = input("Enter player's phone number: ")
            LLPlayers.validate_number(phone_number)
        except ValueError as error:
            print(error)

        try:
            player_email = input("Enter the player's email address: ")
            LLPlayers.validate_email(player_email)
        except ValueError as error:
            print(error)

        try:        
            handle = input("Enter player's handle: ")

        except ValueError as error:
            print(error)

        player = LLPlayers.create_player(name, dob, address, phone_number, player_email, handle)
        print("Player created successfully!")
        return player