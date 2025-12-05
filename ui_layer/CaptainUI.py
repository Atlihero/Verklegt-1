from logic_layer.LL_API import LL_api
from logic_layer.LLPlayers import LLPlayers
from logic_layer.LLTeams import LLTeams


class CaptainUI:
    def __init__(self, LLPlayers, LLTeams):
        self.players = LLPlayers
        self.teams = LLTeams

    def add_player(self, p):
        self.players.add_player(p)

    def add_team(self, t):
        self.teams.create_team(t)


    def add_to_team(self):
        pass

    def remove_from_team(self):
        pass

    def see_player_info(self):
        pass