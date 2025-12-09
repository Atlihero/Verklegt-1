from logic_layer.LL_api import LL_API
from ui_layer.Happy_path import Happy_paths

class Uimain:
    """bleb blob"""
   
    def __init__(self) -> None:
        """sup laddara"""
        LL_api = LL_API()
        self.paths = Happy_paths(LL_api)

    def start(self) -> None:
        """blobmaxing"""
        happy = Happy_paths()
        happy.Happy_create_team()