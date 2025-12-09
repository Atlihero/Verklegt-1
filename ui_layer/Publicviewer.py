from logic_layer.LL_api import LL_API

class PublicViewer:

    def getplayerPublic():
        api = LL_API()        
        players = api.get_playerPublic()
        return players
    
    def getTeamsPublic():
        api = LL_API()
        teams = api.get_teams_public()
        return teams

