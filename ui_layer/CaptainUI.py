from logic_layer.LL_API import LL_api
from logic_layer.LLPlayers import LLPlayers
from logic_layer.LLTeams import LLTeams


class CaptainUI:
    def __init__(self, select_captain, add_player, information_on_captain_team):
        self.select_captain = select_captain
        self.add_player = add_player
        self.information_on_captain_team = information_on_captain_team

    def __str__(self):
        pass