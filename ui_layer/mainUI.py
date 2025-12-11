from logic_layer.LL_api import LL_API
from ui_layer.Happy_path import Happy_paths
from ui_layer.OrganizerUI import OrganizerUI
from ui_layer.Publicviewer import PublicViewer
from ui_layer.CaptainUI import CaptainUI
import os

def clear_term():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

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
        api = LL_API()
        publicViewer = PublicViewer()
        while True:
            Happy_paths.Happy_logo()
            user_inp = input("Press any button to start: ")
            """Here the code starts"""
            if user_inp != 1:
                clear_term()
                Happy_paths.Happy_menu()
                user_inp = input("Enter 1, 2, 3 or q: ")
                
                
                """Here we select Organizer or captain or viewer"""

            
                if user_inp == "1":
                    """Now we are in Organizer and can chose what we will do there"""
                    clear_term()
                    while True:
                        Happy_paths.Happy_organizer() #This is the organizer
                        user_inp = input("Enter 1-6 or q: ")
                        if user_inp == "1": #Here you create a new player
                            clear_term()
                            Happy_paths.Happy_create_player()
                            organizer.create_player()
                            Happy_paths.player_was_made()
                            user_inp = input("Press any button to return to start")
                            if user_inp  != 1:
                                clear_term()
                        elif user_inp == "2": #Here you create a tournament
                            clear_term()
                            Happy_paths.Happy_create_tournament()
                            organizer.createTournament()
                            Happy_paths.tournament_was_made()
                            user_inp = input("Press any button to return to start")
                            if user_inp  != 1:
                                clear_term()
                        elif user_inp == "3": #Here you create a team
                            clear_term()
                            Happy_paths.Happy_create_team()
                            organizer.create_team_ui()
                            Happy_paths.team_was_made()
                            user_inp = input("Press any button to return to start")
                            if user_inp  != 1:
                                clear_term()
                        elif user_inp == "4":
                            clear_term()
                            Happy_paths.Happy_Update_result()
                            organizer.update_result()
                            user_inp = input("Press any button to return to start")
                            if user_inp  != 1:
                                clear_term()
                        elif user_inp == "5": #here you make a player a captain
                            clear_term()
                            Happy_paths.Happy_make_captain()
                            organizer.make_captain()
                            user_inp = input("Press any button to return to start")
                            if user_inp  != 1:
                                clear_term()
                        elif user_inp == "6":
                            clear_term()
                            Happy_paths.Happy_information()
                            organizer.organizer_see_info()
                            user_inp = input("Press any button to return to start")
                            if user_inp  != 1:
                                clear_term()
                        elif user_inp == "q": #return back to starting psition
                            clear_term()
                            self.start()
                        else:
                            clear_term()
                            Happy_paths.not_valid_input()
                
                elif user_inp == "2": #This is the Captain


                    """Now we are in CAPTAIN"""

                    clear_term()
                    Happy_paths.Happy_captain()
                    user_inp = input("Press any button to start")
                    if user_inp  == "1":
                        clear_term()
                        self.start()
                    elif user_inp == "2":
                        clear_term()
                    elif user_inp == "3":
                        clear_term()
                    elif user_inp == "4":
                        clear_term()
                    elif user_inp == "4":
                        clear_term()
                    elif user_inp == "q":
                        clear_term()
                    else:
                        clear_term()
                    


                elif user_inp == "3": #This is the puplic viewer


                    """Now we are in VIWER"""
                    clear_term()
                    while True:
                        Happy_paths.Happy_viewer()
                        user_inp = input("Enter 1, 2, 3 or q: ")
                        if user_inp == "1":
                            publicViewer.getplayerPublic()
                            user_inp = input("Press any button to continue")
                            if user_inp  != 1:
                                clear_term()
                        elif user_inp == "2":
                            self.publicviewer.getTeamsPublic()
                            user_inp = input("Press any button to continue")
                            if user_inp  != 1:
                                clear_term()
                        elif user_inp == "3":
                            self.publicviewer.view_schedule()
                            user_inp = input("Press any button to continue")
                            if user_inp  != 1:
                                clear_term()
                        elif user_inp == "q":
                            clear_term()
                            self.start()
                        else:
                            clear_term()
                            Happy_paths.not_valid_input()
                            
                  
                elif user_inp == "q": #return back to the start


                    """Now we are in EXIT"""


                    clear_term()
                    exit()


                else: # if you enter an invalid input

                    """now this is for invalid input"""
                    #need to find a way to return to input not back or exit
                    clear_term()
                    Happy_paths.not_valid_input()
            
        
            
            else: #restarts the code if you some how manige to give int and not string which should not be possible
                self.start()
                
