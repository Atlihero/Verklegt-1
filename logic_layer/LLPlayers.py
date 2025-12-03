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
                # try:

                # except ValueError:
                #         print("Invalid phone number. Try again.")

        def player_email():
                player_email = input("Enter the player's email address: ")
                pass
                # 6 input línur
        def player_handle():
                handle = input("Enter player's handle: ")
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