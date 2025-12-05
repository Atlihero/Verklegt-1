# from ui_layer.makePlayerUI import get_player_info

# player = get_player_info()
# print(player) 

from data_layer.PlayerIO import PlayerIO
from logic_layer.LLPlayers import LLPlayer
from logic_layer.LLTeams import LLTeams
from ui_layer.CaptainUI import CaptainUI

players = LLPlayer()
teams = LLTeams()

ui = CaptainUI(players, teams)
ui.remove_from_team("Fantom")

# After running, check remaining players:


players = PlayerIO.get_players()
for p in players:
    print(p.name, p.handle, p.team)
