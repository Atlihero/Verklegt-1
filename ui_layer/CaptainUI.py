from logic_layer.LL_API import LL_API
from logic_layer.LLPlayers import LLPlayer
from logic_layer.LLTeams import LLTeams
from logic_layer.LLCaptain import LLCaptain


class CaptainUI:
    def __init__(self, LLPlayers, LLTeams):
        self.players = LLPlayers
        self.teams = LLTeams
        self.ll = LLCaptain()

    def add_player(self, p):
        self.players.add_player(p)

    def add_team(self, t):
        self.teams.create_team(t)


    def add_to_team(self):
        pass
        input ("Who do you want to add to your team?")
        # Input fyrir nafn
        # kalla í fallið add_player frá LLTeams klasa
        # búa til liðslista max 5 á listanum
        # 'do you want to add this person to your team? Y/N'
        # villa ef reynt við 6. manni - Team is full
        # villa ef reynt er að bæta við manni sem er nú þegar í liði


    def remove_from_team(self):
        pass
        input("Who do you want to remove?")
        input("Are you sure you want to remove {name} from the team? Y/N")
        remove_player = input("Please enter the name of the player you want to remove: ")


    def see_player_info(self):
        pass
        input("Choose whose information you want to see.") # setja i menuUI