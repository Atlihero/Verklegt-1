from logic_layer.LL_api import LL_API
from Colors import Colers

class Happy_paths:
    HappyID = 0
    Output_ID = 0
    def Happy_menu():
        print("\033[91m--------------------------------------\033[0m")
        print("\033[91m---           GLADIATORS           ---\033[0m")
        print("\033[91m--------------------------------------\033[0m")
        print("\033[92m---    #Organizer(1)               ---\033[0m")
        print("\033[92m---    #Captain(2)                 ---\033[0m")
        print("\033[92m---    #Puplic viewer(3)           ---\033[0m")
        print("\033[92m---                                ---\033[0m")
        print("\033[92m---    #Please select you option   ---\033[0m")
        print("\033[92m---      (1,2,3 or b for back)     ---\033[0m")
        print("\033[96m--------------------------------------\033[0m")
        print("\033[96m---     #Pleas enter your input    ---\033[0m")
        print("\033[96m--------------------------------------\033[0m")
        print("\033[96m--- Back b)                        ---\033[0m")
        print("\033[96m--------------------------------------\033[0m")
    
    def Happy_viewer():
        print("\033[91m--------------------------------------\033[0m")
        print("\033[91m---           GLADIATORS           ---\033[0m")
        print("\033[91m--------------------------------------\033[0m")
        print("\033[93m---   >Selected viewer             ---\033[0m")
        print("\033[92m---                                ---\033[0m")
        print("\033[92m---    #Information on team(1)     ---\033[0m")
        print("\033[92m---    #Schedule(2)                ---\033[0m")
        print("\033[92m---    #Result(3)                  ---\033[0m")
        print("\033[92m---                                ---\033[0m")
        print("\033[92m---    #Please select you option   ---\033[0m")
        print("\033[92m---      (1,2,3 or b for back)     ---\033[0m")
        print("\033[96m--------------------------------------\033[0m")
        print("\033[96m---     #Pleas enter your input    ---\033[0m")
        print("\033[96m--------------------------------------\033[0m")
        print("\033[96m--- Back b)                        ---\033[0m")
        print("\033[96m--------------------------------------\033[0m")

    def Happy_captain():
        print("\033[91m--------------------------------------\033[0m")
        print("\033[91m---           GLADIATORS           ---\033[0m")
        print("\033[91m--------------------------------------\033[0m")
        print("\033[93m---   >Selected captain            ---\033[0m")
        print("\033[92m---                                ---\033[0m")
        print("\033[92m---       Input captains ID        ---\033[0m")
        print("\033[92m---          from 1-number         ---\033[0m")
        print("\033[92m---                                ---\033[0m")
        print("\033[96m---     #Pleas enter your input    ---\033[0m")
        print("\033[96m--------------------------------------\033[0m")
        print("\033[96m--- Back b)                        ---\033[0m")
        print("\033[96m--------------------------------------\033[0m")

    def Happy_organizer():
        print("\033[91m--------------------------------------\033[0m")
        print("\033[91m---           GLADIATORS           ---\033[0m")
        print("\033[91m--------------------------------------\033[0m")
        print("\033[93m---   >Selected Organizer          ---\033[0m")
        print("\033[92m---                                ---\033[0m")
        print("\033[92m---    #Create player(1)           ---\033[0m")
        print("\033[92m---    #Create tournament(2)       ---\033[0m")
        print("\033[92m---    #Create team(3)             ---\033[0m")
        print("\033[92m---    #Make captain(4)            ---\033[0m")
        print("\033[92m---    (1,2,3,4 or b for back)     ---\033[0m")
        print("\033[96m--------------------------------------\033[0m")
        print("\033[96m---     #Pleas enter your input    ---\033[0m")
        print("\033[96m--------------------------------------\033[0m")
        print("\033[96m--- Back b)                        ---\033[0m")
        print("\033[96m--------------------------------------\033[0m")

    def Happy_create_tournament():
        print("tournament")

    def Happy_create_team():
        print("Create team")

    def Happy_make_captain():
        print("\033[91m--------------------------------------\033[0m")
        print("\033[91m---           GLADIATORS           ---\033[0m")
        print("\033[91m--------------------------------------\033[0m")
        print("\033[93m---   >Selected make captain       ---\033[0m")
        print("\033[92m---                                ---\033[0m")
        print("\033[92m---     $Make player captain$      ---\033[0m")
        print("\033[92m---                                ---\033[0m")
        print("\033[92m---     #Input player ID           ---\033[0m")
        print("\033[96m--------------------------------------\033[0m")
        print("\033[96m---     #Pleas enter your input    ---\033[0m")
        print("\033[96m--------------------------------------\033[0m")
        print("\033[96m--- Back b)                        ---\033[0m")
        print("\033[96m--------------------------------------\033[0m")


    def Happy_create_player():
        print("\033[91m--------------------------------------\033[0m")
        print("\033[91m---           GLADIATORS           ---\033[0m")
        print("\033[91m--------------------------------------\033[0m")
        print("\033[93m---   >Selected create player      ---\033[0m")
        print("\033[92m---                                ---\033[0m")
        print("\033[92m---    #Input players information  ---\033[0m")
        print("\033[92m---                                ---\033[0m")
        print("\033[92m---    #Name                       ---\033[0m")
        print("\033[92m---    #Date of birth              ---\033[0m")
        print("\033[92m---    #email                      ---\033[0m")
        print("\033[92m---    #Phone                      ---\033[0m")
        print("\033[92m---    #gamertag                   ---\033[0m")
        print("\033[96m--------------------------------------\033[0m")
        print("\033[96m--- Back b)                        ---\033[0m")
        print("\033[96m--------------------------------------\033[0m")


    Happy_menu()
    fyrst_input = "" #This code will change just testing
    while fyrst_input != "1" and fyrst_input != "2" and fyrst_input != "3" and fyrst_input !="b":
        print("\033[100mEnter valid Input\033[0m")
        fyrst_input = input("")
    if fyrst_input != "1" and fyrst_input != "2" and fyrst_input != "3" and fyrst_input !="b":
        quit
    elif fyrst_input == "1":
        HappyID = 1
        Happy_organizer()
    elif fyrst_input == "2":
        HappyID = 2
        Happy_captain()
    elif fyrst_input == "3":
        Happy_viewer()
    else:
        print("back")

    if HappyID == 1:
        input2 = input("")
        while input2 != "1" and input2 != "2" and input2 != "3" and input2 !="4" and input2 != "b":
            print("Please select a valid valiu")
        if input2 == "1":
            OD = 1
            Happy_create_player()
        elif input2 == "2":
            OD = 2
            Happy_create_tournament()
        elif input2 == "3":
            OD = 3
            Happy_create_team()
        elif input2 == "4":
            OD = 4
            Happy_make_captain()
        



def scoobster(pink, reset, blue, neonblue, Yellow, gray, red, highlite, neongreen):
    print(pink,"########################")
    print(pink,"## ",highlite,"--Scooby doo--",reset,pink,"##")

scoobster(*Colers.all_colers())