from logic_layer.LL_api import LLAPI
from logic_layer.LLPlayers import LLPlayers
from logic_layer.LLStatistics import LLStatistics
from logic_layer.LLTeams import LLTeams
from logic_layer.LLTournament import LLTournament

class MainUI:
    def __init__(self, LLAPI):
        self.api = LLAPI
        self.players = LLPlayers()
        self.statistics = LLStatistics()
        self.teams = LLTeams()
        self.tournaments = LLTournaments()
