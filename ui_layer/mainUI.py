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
        paths = Happy_paths
        while True:
            paths.Happy_logo()
            user_inp = input("Press any button to start: ")
            """Here the code starts"""
            if user_inp != 1:
                paths.Happy_menu()
                user_inp = input("Enter 1, 2, 3 or b: ")
                
                
                """Here we select Organizer captain viewer"""

                if user_inp == "1":
                    paths.Happy_organizer()
                    user_inp = input("Enter 1, 2, 3, 4 or b: ")
                    if user_inp == "1":
                        paths.Happy_create_player()
                        exit()
                elif user_inp == "2":
                    paths.Happy_captain()
                    user_inp = input("")
                    exit()
                elif user_inp == "3":
                    paths.Happy_viewer()
                elif user_inp == "b":
                    os.system('cls')
                    continue
                else:
                    exit()
            else:
                exit()
