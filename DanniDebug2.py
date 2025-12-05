from logic_layer.LL_api import LL_API

PLAYER_PATH = r"data_layer\_data\Players.csv"
TEAM_PATH = r"data_layer\_data\Teams.csv"
TOURNAMENT_PATH = r"data_layer\_data\Tournament.csv"
GAMES_PATH = r"data_layer\_data\Games.csv"

userinput = int(input("Veldu ID leikmanns: "))
def getplayer():
    api = LL_API()        
    players = api.getplayers()
    return players

player_dict = getplayer()
print(player_dict[userinput])
