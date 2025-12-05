from logic_layer.LL_api import LL_API

class PublicViewer:
    
    userinput = int(input("Veldu ID leikmanns milli 1-57: "))
    def getplayerPublic():
        api = LL_API()        
        players = api.getPlayerPublic()
        return players

    player_dict = getplayerPublic()
    print(player_dict[userinput])
