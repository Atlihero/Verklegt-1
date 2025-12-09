from logic_layer.LL_api import LL_API
from ui_layer.Happy_path import Happy_paths

class Uimain:
    """This class suplies information from logic layer to its correct 
    location and gives restrictions depending of user input"""
    def __init__(self) -> None:
        """gets logic_layer as a variable"""
        LL_api = LL_API()
        

    def start(self) -> None:
        """Prints the game screen on terminal and controles the flow of information"""
        paths = Happy_paths
        return paths.Happy_logo()
