from logic_layer.LL_API import LL_API
from logic_layer.LLPlayers import LLPlayer
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
        input ("Who do you want to add to your team?")


    def remove_from_team(self):
        pass
        input("Who do you want to remove?")
        input("Are you sure you want to remove {name} from the team? Y/N")


    def see_player_info(self):
        pass
        input("Choose whose information you want to see.") # setja i menuUI