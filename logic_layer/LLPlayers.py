#from Models.Player import Player
from datetime import datetime

class PlayerInfo():

        def dob_player():
                player_dob = input("Enter player date of birth (DD/MM/YYYY): ")
                try:
                        entered_date = datetime.strptime(player_dob, "%d/%m/%Y")
                       
                        if entered_date > datetime.now():
                               print("Please enter a valid date.")
                               return PlayerInfo.dob_player()
                        
                        else:
                                day = entered_date.day
                                month = entered_date.month
                                year = entered_date.year
                                print(f"{day}/{month}/{year}")
                except ValueError:
                        print("Invalid date. Try again using DD/MM/YYYY.")
                        return PlayerInfo.dob_player()


        def player_information():
                pass
                # 6 input línur
                player_name = input("Enter full name of player: ")
                player_address = input("Enter player's home address: ")
                player_phone = input("Enter player's phone number: ")
                player_email = input("Enter the player's email address: ")
                player_handle = input("Enter player's handle: ")
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

player = PlayerInfo.dob_player()
print(player)