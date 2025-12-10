from logic_layer.LL_api import LL_API
from ui_layer.Happy_path import Happy_paths
from ui_layer.OrganizerUI import OrganizerUI
from ui_layer.Publicviewer import PublicViewer
from ui_layer.CaptainUI import CaptainUI
import os

class Uimain:
    """This class suplies information from logic layer to its correct 
    location and gives restrictions depending of user input"""
    def __init__(self) -> None:
        """gets logic_layer as a variable"""
        LL_api = LL_API()
        self.captain = CaptainUI()
        self.publicviewer = PublicViewer()
        self.organizer = OrganizerUI()
        
        


    def start(self) -> None:
        """Prints the game screen on terminal and controles the flow of information"""
        Happy_paths
        organizer = OrganizerUI()
        captain = CaptainUI()
        api = LL_API()
        while True:
            Happy_paths.Happy_logo()
            user_inp = input("Press any button to start: ")
            """Here the code starts"""
            if user_inp != 1:
                Happy_paths.Happy_menu()
                user_inp = input("Enter 1, 2, 3 or b: ")
                
                
                """Here we select Organizer or captain or viewer"""

                if user_inp == "1":
                    """Now we are in Organizer and can chose what we will do there"""
                    Happy_paths.Happy_organizer() #This is the organizer
                    user_inp = input("Enter 1, 2, 3, 4 or b: ")
                    if user_inp == "1": #Here you creata a new player
                        Happy_paths.Happy_create_player()
                        organizer.create_player()
                        exit()
                    elif user_inp == "2": #Here you create a tournament
                        Happy_paths.Happy_create_tournament()
                        organizer.createTournament()
                        exit()
                    elif user_inp == "3": #Here you create a team
                        Happy_paths.Happy_create_team()
                        api.add_team()
                        exit()
                    elif user_inp == "4": #here you make a player a captain
                        Happy_paths.Happy_make_captain()
                        api.select_captains()
                    elif user_inp == "b": #return back to starting position
                        os.system('cls')
                        continue



                elif user_inp == "2": #This is the Captain
                    Happy_paths.Happy_captain()
                    # first pick which captain (this also sets current_team_name)
                    if not captain.select_captain_and_team():
                        continue # go back to main menue if captain not foudn
                    
                    Happy_paths.Happy_captain_add_or_info()
                    cap_choice = input("").strip().lower()

                    if cap_choice == "1":
                        captain.add_to_team()
                    elif cap_choice == "2":
                        captain.remove_from_team()
                    elif cap_choice == "3":
                        captain.cap_see_player_info()
                    elif cap_choice == "b":
                        os.system("cls")
                        continue





                    """if user_inp == "1": #Here you Add Player to Team
                        Happy_paths.Happy_captain_add_or_info()
                        captain.add_to_team()
                        exit() 
                        

                    if user_inp == "2": #Here you See Information on Captains
                        Happy_paths.Happy_captain_player_to_inspect()
                        captain.cap_see_player_info()
                        
                        if user_inp == "x": #Here you Select Player To Inspect
                            Happy_paths.Happy_captain_inspecting_information()
                            captain.cap_see_player_info()
                           

                            if user_inp == "x": #Here you Select Information
                                x



                    elif user_inp == "b": #return back to starting position
                        os.system('cls')
                        continue   """













                    
                elif user_inp == "3": #This is the puplic viewer
                    Happy_paths.Happy_viewer()
                elif user_inp == "b": #return back to the start
                    os.system('cls')
                    continue
                else: # if you enter an invalid input
                    print("invalid input")
                    #need to find a way to return to input not back or exit
                    exit()
            else: #stops the code if you some how manige to give int not string which should not be possible
                exit()
