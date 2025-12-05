from logic_layer.LL_API import LLAPI
from logic_layer.LLPlayers import LLPlayer
from logic_layer.LLStatistics import LLStatistics
from logic_layer.LLTeams import LLTeams


class MainUI:
    def __init__(self, LLAPI):
        self.api = LLAPI
        self.players = LLPlayer()
        self.statistics = LLStatistics()
        self.teams = LLTeams()

    def api_logic(self, api):
        self.add_api(api)

    def add_player(self, players):
        self.players.add_player(players)

    def add_team(self, team):
        self.teams.create_team(team)
