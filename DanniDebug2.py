from logic_layer.LL_api import LL_API


userinput = int(input("Veldu ID leikmanns milli 1-57: "))
def getplayer():
    api = LL_API()        
    players = api.getplayers()
    return players

player_dict = getplayer()
print(player_dict[userinput])
