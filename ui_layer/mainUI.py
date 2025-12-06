from logic_layer.LL_api import LL_API


class MainUI:
    def __init__(self):
        self.api = LL_API()

    def api_logic(self, api):
        self.add_api(api)

    def add_player(self, players):
        self.players.add_player(players)

    def add_team(self, team):
        self.teams.create_team(team)