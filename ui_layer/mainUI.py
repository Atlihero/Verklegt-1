from logic_layer.LL_api import LL_API
from logic_layer.LLPlayers import LLPlayer
from logic_layer.LLTeams import LLTeams


class CaptainUI:
    def __init__(self):
        self.api = LL_API()
        self.players = LLPlayer()
        self.teams = LLTeams()

    def api_logic(self, api):
        self.add_api(api)

    def add_player(self, players):
        self.players.add_player(players)

    def add_team(self, team):
        self.teams.create_team(team)
