from logic_layer.LL_api import LL_api
from logic_layer.LLPlayers import LLPlayers
from logic_layer.LLTeams import LLTeams


class CaptainUI:
    def __init__(self):
        self.api = LL_api()
        self.players = LLPlayers()
        self.teams = LLTeams()

    def api_logic(self, api):
        self.add_api(api)

    def add_player(self, players):
        self.players.add_player(players)

    def add_team(self, team):
        self.teams.create_team(team)
