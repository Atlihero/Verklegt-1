#from Models.Player import Player
from datetime import datetime

class PlayerInfo():

        def player_name():
                name = input("Enter full name of player: ")
                return name
        
        def player_dob():
                dob = input("Enter player date of birth (DD/MM/YYYY): ")
                try:
                        entered_date = datetime.strptime(dob, "%d/%m/%Y")
                       
                        if entered_date > datetime.now():
                               print("Please enter a valid date.")
                               return PlayerInfo.player_dob()
                        
                        else:
                                day = entered_date.day
                                month = entered_date.month
                                year = entered_date.year
                                print(f"{day}/{month}/{year}")
                except ValueError:
                        print("Invalid date. Try again using DD/MM/YYYY.")
                        return PlayerInfo.player_dob()

                
        def player_address():
                address = input("Enter player's home address: ")
                return address
        
        def player_phone():
                pass
                # phone_number = input("Enter player's phone number: ")
                # þarf að vera 7 tölustafir
                # try:

                # except ValueError:
                #         print("Invalid phone number. Try again.")

        def player_email():
                '''Asks the player for an email address and checks if it is valid so he can continue
                adding his information. Prints error messages when the input is not up to standards.'''

                player_email = input("Enter the player's email address: ")
                try:
                        local_name, domain = player_email.split("@")
                                
                except ValueError:
                        if player_email.count("@") > 1:
                                print("Email can only have 1 '@'. Please try again.")
                        else:
                                print("Email has to contain '@'. Please try again.")
                        return PlayerInfo.player_email()
                
                if not local_name:
                        print("Local part (name) may not be empty. Please try again")
                        return PlayerInfo.player_email()
                
                domain_parts = domain.split(".")
                if len(domain_parts) < 2 or not domain_parts[0] or not domain_parts[1]:
                        print("Domain must have a name and a valid ending. Please try again.")
                        return PlayerInfo.player_email()
                
                ending = domain.split(".")[-1]
                if len(ending) < 2 or len(ending) > 3 or not ending.isalpha():
                        print("The email must contain a valid ending. Please try again.")
                        return PlayerInfo.player_email()
       
                return f"{player_email} is a valid email"

        def player_handle():
                pass
                #handle = input("Enter player's handle: ")
                        # búa til lista
                        # 

        
        def edit_player():
                "fyrirliði vill breyta upplýsingum leikmanns í liði síns"
                pass

        def create_player():
                "Skipuleggjandi vill búa til leikmann"
                pass




# eitt fall fyrir það sem player slær inn
        # def player_information
# muna eftir að hafa villuboð
# 

player = PlayerInfo.player_email()
print(player)