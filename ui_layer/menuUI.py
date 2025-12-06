from logic_layer.LL_api import LL_API

class MainMenu:
    
    def __init__(self):
        self.api = LL_API()
    
    def getplayer(self):
        LL_API.getplayers()