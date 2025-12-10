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
                    user_inp = input("Enter 1-6 or b: ")
                    if user_inp == "1": #Here you create a new player
                        organizer.create_player(self)
                        exit()
                    elif user_inp == "2": #Here you create a tournament
                        organizer.createTournament(self)
                        exit()
                    elif user_inp == "3": #Here you create a team
                        organizer.create_team_ui(self)
                    elif user_inp == "4":
                        organizer.update_result(self)
                        exit()
                    elif user_inp == "5": #here you make a player a captain
                        Happy_paths.Happy_make_captain()
                    elif user_inp == "6":
                        organizer.organizer_see_info(self)
                        exit()
                    elif user_inp == "b": #return back to starting psition
                        os.system('cls')
                        continue
                
                elif user_inp == "2": #This is the Captain


                    """Now we are in CAPTAIN"""


                    Happy_paths.Happy_captain()
                    user_inp = input("")
                    exit()


                elif user_inp == "3": #This is the puplic viewer


                    """Now we are in VIWER"""
                    Happy_paths.Happy_viewer()
                    user_inp = input("Enter 1, 2, 3 or b")
                    if user_inp == "1":
                        print("nice guys")#information on teams
                        api.get_teams_public()
                    elif user_inp == "2":
                        print("epic")#schedual
                        api.scheduleGames()
                        exit()
                    elif user_inp == "3":
                        print("123") #result
                        
                        exit()
                    else:
                        self.start()
                        exit()
                  


                elif user_inp == "b": #return back to the start


                    """Now we are in EXIT"""


                    clear_term()
                    self.start()


                else: # if you enter an invalid input

                    """now this is for invalid input"""
                    #need to find a way to return to input not back or exit
                    print("invalid input")
                    user_inp = input("Press any button to exit:")
                    if user_inp != 1:
                        clear_term()
                        self.start()
                        
                    
            
            else: #stops the code if you some how manige to give int not string which should not be possible
                self.start()
                
